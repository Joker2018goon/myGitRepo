import re

regex = re.compile('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,10}$')
match = regex.match('    ')
if match:
    print('true')
else:
    print('false')