from colored import fg, bg, attr

PREFIX = '[DCLI]'

def jump():
    print()

def paragraph(content):
    print('\t' + content)

def prefix():
    return attr('bold') + bg(208) + PREFIX + attr('reset') + ' ' + attr('bold')

def error(msg):
    print((prefix() + '%s' + msg + '%s') % (fg(1), attr(0)))

def info(msg):
    print(prefix() + msg + attr('reset'))

