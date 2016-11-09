import re
m = (re.match( 'string goes here'))
if m:
    print ('Match found: ', m.group())
else:
    print ('No match')
