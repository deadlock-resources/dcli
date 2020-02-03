
import json

import inquirer

from dcli.generator import file

METHOD_NAME = 'METHOD_NAME'

FILE_NAME = 'FILE_NAME'

GENERIC = 'Generic'

ARRAY_DIMENSION = 'number'

TYPE_NAME = 'name'

CLASS_NAME = 'className'

ARRAY = 'Array'

CONTINUE = 'continue'

YES = 'Yes'

NO = 'No'

PARAM_NAME = 'paramName'

TYPE = 'type'

PARAMETRIZED_TYPE = 'Type to parametrize (eg a list)'

KNOWN_LIB_LANGUAGE_TYPE = 'Existing type from language lib'
OWN_TYPE = 'Your own type'


def get_datatype_from_user(language_id,
                           filename,
                           have_generics=True,
                           have_parametrized=True,
                           allow_type_creation=True,
                           allow_lib=True):
    print(language_id + 'and file name is : ' + filename)
    json_file = file.openFile(language_id, 'resources' + '/' + filename)
    return select_types_from_json(json_file=json_file,
                                  have_generics=have_generics,
                                  have_parametrized=have_parametrized,
                                  allow_type_creation=allow_type_creation,
                                  allow_lib=allow_lib)


def select_examples_from_json(json_file):
    loaded_examples = json.load(json_file)
    examples = []
    for currentType in loaded_examples:
        examples.append(currentType[CLASS_NAME])
    return loaded_examples


def select_types_from_json(json_file,
                           have_generics=True,
                           have_parametrized=True,
                           allow_type_creation=True,
                           allow_lib=True):
    loaded_types = json.load(json_file)
    types_to_choose = []
    for currentType in loaded_types:
        name_ = currentType[TYPE_NAME]
        types_to_choose.append(name_)
    if allow_lib:
        types_to_choose.append(KNOWN_LIB_LANGUAGE_TYPE)
    if allow_type_creation:
        types_to_choose.append(OWN_TYPE)
    if have_generics:
        types_to_choose.append(GENERIC)
    if have_parametrized:
        types_to_choose.append(PARAMETRIZED_TYPE)

    types_to_choose.append(ARRAY)
    file_question = [
        inquirer.Text(FILE_NAME, message='Type the wanted file name without extension'),
        inquirer.Text(METHOD_NAME, message='Type the method name')
    ]
    answers = inquirer.prompt(file_question)
    file_name = answers[FILE_NAME]
    method_name = answers[METHOD_NAME]
    method_return_type = handle_param_or_return(False, types_to_choose)
    parameters = handle_param_or_return(True, types_to_choose)
    return StructureHolder(structure_name=file_name,
                           file_names=[file_name],
                           methods=[MethodHolder(method_name=method_name,
                                                 return_type=method_return_type[0],
                                                 method_parameters=parameters)])


def handle_param_or_return(is_arg, types_dict, fresh_start=False):
    if is_arg:
        if fresh_start is True:
            ret = handle_method_param(is_arg, types_dict, previous_arg=[])
        else:
            ret = handle_method_param(is_arg, types_dict)

    else:
        ret = [get_user_type(is_it_param=is_arg, types_dict=types_dict, currentKindOftype='method return')]
    current_res = ''.join(map(str, ret))
    if not does_user_continue('Are you satisfied with your choice ? ' + current_res):
        print('Restart choice')
        ret = handle_param_or_return(is_arg, types_dict, True)
    else:
        print(current_res)
    return ret


def handle_method_param(is_arg, current_dict, previous_arg=[]):
    print("current args : " + str(previous_arg))
    previous_arg.append(get_user_type(is_it_param=is_arg, types_dict=current_dict, currentKindOftype='method parameter'))
    if does_user_continue("Do you need an other parameter ?"):
        handle_method_param(is_arg, current_dict, previous_arg)
    return previous_arg


def does_user_continue(parameter_="Do you want to continue"):
    continue_questions = [
        inquirer.List(CONTINUE,
                      message=parameter_,
                      choices=[NO, YES],
                      ),
    ]
    answer = inquirer.prompt(continue_questions)
    return answer[CONTINUE] == YES


def select_type_from_dict(question_msg='What type do you need ?', types_dict=[]):
    questions = [
        inquirer.List(TYPE,
                      message=question_msg,
                      choices=types_dict,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers


def get_user_type(is_it_param, types_dict, is_sub_type=False, sub_types_dic=None, parent_name='', currentKindOftype='required'):
    types_to_display = sub_types_dic if is_sub_type is True or sub_types_dic else types_dict
    answers = select_type_from_dict(
        question_msg='What is the ' + currentKindOftype+ ' type ?',
        types_dict=types_to_display)
    type_ = answers[TYPE]
    type_need_creation = False
    type_need_import = False
    is_array = False
    array_dim = 0
    array_type = ''
    parametrized_root_type = ''
    parametrized_types = []
    param_name = ''
    is_generic = False
    if type_ == OWN_TYPE:
        new_questions = [
            inquirer.Text(TYPE, message='Type your new full type name')
            # validate=lambda text: len(text) > 0 or 'Must not be empty.')
        ]
        type_ = inquirer.prompt(new_questions)[TYPE]
        type_need_creation = True
        type_need_import = True
        # if does_user_continue("Do you want to parametrize this type"):
        #     get

    elif type_ == KNOWN_LIB_LANGUAGE_TYPE:
        new_questions = [
            inquirer.Text(TYPE, message='Type the lib language full type name')
        ]
        type_ = inquirer.prompt(new_questions)[TYPE]
        type_need_creation = False
        type_need_import = True
    elif type_ == GENERIC:
        new_questions = [
            inquirer.Text(TYPE, message='Type the generic type name')
        ]
        is_generic = True
        type_ = inquirer.prompt(new_questions)[TYPE]

    elif type_ == ARRAY:
        reduced_type_list = types_dict.copy()
        reduced_type_list.remove(ARRAY)
        array_question = [inquirer.List(ARRAY_DIMENSION,
                                        message="What is the number of dimension of your array ?",
                                        choices=[1, 2, 3, 4, 5],
                                        )]
        array_dim = inquirer.prompt(array_question)[ARRAY_DIMENSION]
        array_type = get_user_type(is_it_param=is_it_param, types_dict=types_dict, is_sub_type=True,
                                   sub_types_dic=reduced_type_list, currentKindOftype='array').type_name
        print("sub type selected is  " + array_type)

        is_array = True

    elif type_ == PARAMETRIZED_TYPE:
        reduced_type_list = types_dict.copy()
        reduced_type_list.remove(ARRAY)
        reduced_type_list.remove(PARAMETRIZED_TYPE)
        parametrized_root_type = get_user_type(is_it_param=is_it_param, types_dict=types_dict, is_sub_type=True,
                                               sub_types_dic=reduced_type_list, currentKindOftype='to parametrize').type_name
        print("base type selected is  " + str(parametrized_root_type))
        parametrized_types.append(get_user_type(is_it_param=is_it_param, types_dict=types_dict, is_sub_type=True,
                                                sub_types_dic=reduced_type_list, currentKindOftype='parametrized').type_name)
        while does_user_continue("Do you need an other parameter type"):
            parametrized_types.append(get_user_type(is_it_param=is_it_param, types_dict=types_dict, is_sub_type=True,
                                                    sub_types_dic=reduced_type_list, currentKindOftype='parametrized').type_name)
            print("sub types are  " + str(parametrized_types))
    if is_it_param and not is_sub_type:
        param_name = get_param_name()
    elif is_sub_type:
        param_name = parent_name

    ret = DataTypeHolder(type_name=type_,
                         need_import=type_need_import,
                         need_creation=type_need_creation,
                         is_arg=is_it_param,
                         arg_name=param_name,
                         is_array=is_array,
                         array_dim=array_dim,
                         array_type=array_type,
                         parametrized_root_type=parametrized_root_type,
                         paramTypes=parametrized_types,
                         is_generic=is_generic)

    return ret


def get_param_name():
    arg_questions = [
        inquirer.Text(PARAM_NAME, message="What is the parameter name ?")
    ]
    return inquirer.prompt(arg_questions)[PARAM_NAME]


class DataTypeHolder:
    def __init__(self, type_name, need_import, need_creation, is_arg, arg_name='', is_generic=False, paramTypes=[],
                 parametrized_root_type='',
                 is_array=False, array_dim=1, array_type=''):
        self.parametrized_root_type = parametrized_root_type
        self.array_type = array_type
        self.type_name = type_name
        self.need_import = need_import
        self.need_creation = need_creation
        self.is_arg = is_arg
        self.arg_name = arg_name
        self.is_generic = is_generic
        self.parameters_types = paramTypes
        self.is_array = is_array
        self.array_dim = array_dim

    def add_parameter_type(self, type_name):
        self.parameters_types.append(type_name)

    def __str__(self):
        ret = ''
        ret += '['
        if self.is_array:
            ret += self.array_type
            for i in range(0, self.array_dim):
                ret += '[]'
        elif len(self.parameters_types) > 0:
            ret += self.parametrized_root_type + '<'
            param_length = len(self.parameters_types)
            for i in range(0, param_length):
                if param_length > 1 and i > 0:
                    ret += ',' + self.parameters_types[i]
                else:
                    ret += self.parameters_types[i]
            ret += '>'
        else:
            ret += self.type_name
        if self.is_arg:
            ret += ' ' + self.arg_name
        ret += ']'
        return ret


class StructureHolder:
    def __init__(self, structure_name, file_names, methods, attributes=[]):
        self.file_names = file_names
        self.structure_name = structure_name
        self.methods = methods
        self.attributes = attributes

    def __str__(self):
        return json.dumps(self, default=lambda x: x.__dict__)
        # return self.structure_name + ' ' + str(self.methods)


class MethodHolder:
    def __init__(self, method_name, return_type, method_parameters=[]):
        self.return_type = return_type
        self.method_parameters = method_parameters
        self.method_name = method_name


