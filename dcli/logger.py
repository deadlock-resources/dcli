from colored import fg, bg, attr

PREFIX = '[DCLI] '

def error(msg):
    print (PREFIX + '%s msg %s' % (fg(1), attr(0)))

def info(msg):
    print(PREFIX + msg)

