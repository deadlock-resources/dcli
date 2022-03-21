import time
import os
import sys
import json
import uuid
import requests
import hashlib
import shutil
import tempfile
from multiprocessing import Process
from .model.missionUserScore import MissionUserScore
from .generator.file import get_path_from_root, load_yaml, create_tmp_folder, write_file
from .spinCursor import SpinCursor
from .logger import info, error, jump
from .const import CHALLENGE_YAML, API_PORT, MISSION_USER_SCORE_ENDPOINT, MISSION_USER_SCORE_FILENAME, API_ADRESS
from .scoreController import startScoreResource
from .cmd import execute
from .generator.file import get_path_from_root

from distutils.dir_util import copy_tree

DOCKER_NETWORK = 'deadlock-challenge'
PREFIX_SERVICE_NAME = 'deadlock-service'
PERSIST_DOCKER_NAME = "deadlock-persist-mission"


def build(tag, path, verbose=False):
    spin = SpinCursor('', speed=5, maxspin=100000)
    if (os.path.exists(path) == False):
        error('Directory does not exist ' + path)
        sys.exit(1)
    info('🔨 Building mission..')
    spin.start()

    if (os.path.exists(f'{path}/build.sh')):
        execute(f'{path}/build.sh', {
            'exitOnError': True,
            'messageOnError': 'Cannot execute build.sh file',
            'spin': spin})
    info('🐳 Building Docker image')
    execute(f'docker build {path} {quiet_docker_build(verbose)} -t {tag}', {
        'quiet': not verbose,
        'exitOnError': True,
        'spin': spin})

    execute(f'docker network create {DOCKER_NETWORK}', {'quiet': not verbose})

    # also build services if exist
    if os.path.exists(f'{path}/services') == True:
        dirs = os.listdir(f'{path}/services')
        for service in dirs:
            build_and_run_service(f'{path}/services', service,verbose)

    spin.stop()


def quiet_docker_build(verbose):
    return "-q" if not verbose else ""


def build_and_run_service(path, service,verbose):
    info(f'📂 {service} service found')
    info(f'>  🐳 Building {service}')
    execute(f'docker build {quiet_docker_build(verbose)} -f {path}/{service}/Dockerfile -t {get_docker_service_name(service)} {path}/{service}',
            {"quiet": False, "exitOnError": True, "messageOnError": f'Building {service} failed'})
    info(f'>  🚀 Running {service}')
    execute(f'docker run -d --rm --net={DOCKER_NETWORK} --name {service} {get_docker_service_name(service)}',
            {"quiet": False, "exitOnError": True, "messageOnError": f'Running {service} failed'})


def get_docker_service_name(serviceName):
    return f'{PREFIX_SERVICE_NAME}-{serviceName}'


def clean(verbose=False):
    print('')
    time.sleep(1)
    info('Cleaning resources')
    execute(f'docker ps --filter network={DOCKER_NETWORK} -aq | xargs -r docker stop >/dev/null | xargs -r docker rm',
            {"quiet": not verbose})
    execute(f'docker network rm {DOCKER_NETWORK}', {"quiet": not verbose})
    info('Done')


def prepare_metamorph_code(path, tmpDir,verbose):
    info('🔨 Building mission..')
    spin = SpinCursor('', speed=5, maxspin=100000)
    spin.start()

    try:
        copy_tree(path, tmpDir)
        shutil.copy(get_path_from_root('utils/Dockerfile-runner'), tmpDir + '/Dockerfile')
        shutil.copy(get_path_from_root('utils/run.sh'), tmpDir + '/run.sh')

        # copy each template files
        for subdir, dirs, files in os.walk(path + '/template'):
            for file in files:
                shutil.copy(os.path.join(subdir, file), tmpDir)

        os.system('docker build ' + tmpDir + f' {quiet_docker_build(verbose)} -t meta')
    finally:
        spin.stop()


def run_metamorph_code(path, language,verbose):
    exec_metamorph_code(path, language, 'run',verbose)


def solve_metamorph_code(path, language,verbose):
    exec_metamorph_code(path, language, 'solve',verbose)


def exec_metamorph_code(path, language, way,verbose):
    if path == '.':
        path = os.getcwd()
    elif path[0] != '/':
        error('Path given must be absolute')
        exit(1)

    download_if_necessary(path)

    # copy everything to tmp to avoid any conflict with user directory files
    # cannot use the default /tmp dir, because it generate problem with Docker volume
    tmpDir = f'{path}/build'
    prepare_metamorph_code(path, tmpDir,verbose)

    # volume to the tmp dir
    os.system(f"docker run -v {tmpDir}:/tmp/runner meta {way} {language}")
    shutil.rmtree(tmpDir, ignore_errors=True)


def download_if_necessary(path):
    should_download = True
    if os.path.exists(path + '/runner'):
        if os.path.exists(path + '/.hash'):
            entry_hash = open(path + '/.hash', 'r').read()
            if entry_hash == hashlib.md5(open('entry.rs', 'rb').read()).hexdigest():
                should_download = False

    if should_download == True:
        download_runner(path)


def download_runner(path):
    url = "https://builder.staging.deadlock.io/build"

    info('🛰️  Download runner based on your entry.rs file.')
    info('Operation will be long the first time, no worries.')

    spin = SpinCursor('', speed=5, maxspin=100000)
    spin.start()
    runner_bin = 'runner'
    files = {'file': open('entry.rs', 'rb')}
    response = requests.post(url, files=files, stream=True)
    spin.stop()

    if response.status_code != 200:
        print(response.text)
        print(response.content)
        error('Cannot build your entry.rs, check its correct.')
        exit(1)

    with open(runner_bin, 'wb') as f:
        shutil.copyfileobj(response.raw, f)

    os.system('chmod u+x runner')

    # write runner hash
    with open(path + '/.hash', 'w+') as f:
        with open('entry.rs', 'rb') as entry:
            h = hashlib.md5(entry.read()).hexdigest()
            f.write(h)

    info('🛰️  Download completed')


def run_code(path=os.getcwd(), verbose=False):
    tag = uuid.uuid4()
    build(tag, path, verbose)
    info('🚀 Running mission..')
    execute(f'docker run --net={DOCKER_NETWORK} {tag} Run')
    pass


def run_hack(path=os.getcwd()):
    os.system(get_path_from_root('utils/run-hack.sh'))


def run_persist(path=os.getcwd(), verbose=False):
    info('Remove previous mission..')
    execute(f'docker rm {PERSIST_DOCKER_NAME} -f', {'quiet': not verbose})

    yaml = load_yaml(path + '/' + CHALLENGE_YAML)

    ports = yaml['persistent']['ports']
    portsCmd = ''
    webPortFound = False
    userConfigPath = get_path_from_root('utils/user-challenge.json');

    with open(userConfigPath, 'r+') as f:
        jsonContent = json.load(f)
        jsonContent['paths'] = {}
        for key in ports:
            portsCmd += f' -p {ports[key]}:{ports[key]}'
            if ports[key] == 3000:
                webPortFound = True
            else:
                jsonContent['paths'][key] = str(ports[key])
        f.seek(0)
        json.dump(jsonContent, f, indent=2)
        f.truncate()

    if webPortFound == False:
        error('Your must include web port in the challenge.yaml file: web: 3000')
        sys.exit(1)

    # start docker container
    tag = uuid.uuid4()
    build(tag, path, verbose)
    info('🚀 Running mission..')

    execute(
        f'docker run --net={DOCKER_NETWORK} -v {userConfigPath}:/home/config/user-challenge.json -d {portsCmd} --name {PERSIST_DOCKER_NAME} {tag}',
        {'quiet': not verbose, 'exitOnError': True})
    info('🌐 You can view the mission in the browser:')
    info('🌐 http://localhost:3000')

    while True:
        try:
            sys.stdin.readline()
        except KeyboardInterrupt:
            info('Cleaning mission..')
            execute(f'docker rm {PERSIST_DOCKER_NAME} -f', {'quiet': not verbose})
            clean(verbose)
            sys.exit()


def solve_score(tag, path=os.getcwd()):
    '''
    Run Solve step for the mission under given path.
    As if user clicked on Submit button.
    Create and mount all necessaries files to be able to post the score somewhere.

    :param path: path of your mission. Default is .
    '''
    info('Setting up environment..')

    info('Starting http server..')
    httpServerProcess = Process(target=startScoreResource)
    httpServerProcess.start()

    info('Writing file..')
    tmpPathFile = create_tmp_folder() + '/' + MISSION_USER_SCORE_FILENAME
    missionUserScore = MissionUserScore(str(uuid.uuid4()),
                                        f'http://{API_ADRESS}:{str(API_PORT)}{MISSION_USER_SCORE_ENDPOINT}').__dict__
    missionUserScoreJson = json.dumps(missionUserScore)
    write_file(tmpPathFile, missionUserScoreJson)

    info('Starting mission score..')
    os.system(f'docker run --network="host" -v {tmpPathFile}:/tmp/{MISSION_USER_SCORE_FILENAME} {tag} Solve')
    httpServerProcess.terminate()


def solve_code(tag, path=os.getcwd()):
    info('🚀 Solving mission..')
    os.system(f'docker run --net={DOCKER_NETWORK} {tag} Solve')
    pass


def solve(path=os.getcwd(), language='empty', verbose=False):
    '''
    Run Solve step for the mission under given path.
    As if user clicked on Submit button.

    :param path: path of your mission. Default: .
    '''
    exit_if_no_challenge_file(path)
    yaml = load_yaml(path + '/' + CHALLENGE_YAML)
    if 'coding' in yaml:
        if yaml['type'] == 'PERSISTENT':
            error('Cannot solve PERSISTENT mission, try run instead.')
            sys.exit(1)
        elif os.path.exists(path + '/entry.rs') == True:
            solve_metamorph_code(path, language,verbose)
        elif 'score' in yaml['coding']:
            tag = uuid.uuid4()
            build(tag, path, verbose)
            solve_score(tag, path)
        else:
            tag = uuid.uuid4()
            build(tag, path, verbose)
            solve_code(tag, path)
    else:
        error('Challenge type not supported for solve method.')
    clean(verbose)


def run(path=os.getcwd(), language='empty', verbose=False):
    '''
    Run the mission under given path.
    As if user clicked on Run button.

    :param path: path of your mission. Default: .
    '''
    exit_if_no_challenge_file(path)
    yaml = load_yaml(path + '/' + CHALLENGE_YAML)
    if yaml['type'] == 'PERSISTENT':
        run_persist(path, verbose)
    elif 'coding' in yaml:
        if os.path.exists(f'{path}/entry.rs') == True:
            run_metamorph_code(path, language,verbose)
        else:
            run_code(path, verbose)
    elif 'hacking' in yaml:
        run_hack(path)
    else:
        error('Challenge type not supported, verify your challenge.yaml')
    clean(verbose)


def exit_if_no_challenge_file(path):
    if os.path.exists(path + '/' + CHALLENGE_YAML) == False:
        error('You have to be within a challenge folder to execute your command.')
        sys.exit(1)
