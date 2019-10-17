from colored import fg, bg, attr

PREFIX = '[DCLI]'

def jump():
    print()

def paragraph(content):
    print(content)

def error(msg):
    print((PREFIX + '%s' + msg + '%s') % (fg(1), attr(0)))

def info(msg):
    print(attr('bold') + bg(208) + PREFIX + attr('reset') + ' ' + attr('bold') + msg + attr('reset'))

