import re
a = {1 : (lambda x: re.match(r'([A-Za-z])', x)),
     2 : (lambda x: re.findall(r'([A-Za-z0-9.-])', x)),
     3 : (lambda x: re.findall(r'\w', x[-1])),
     4 : (lambda x: len(min(x)) if len(min(x)) == 1 else False),
     5 : (lambda x: len(x) if len(x) == 20 else False)
     }

#print(a[number_key]("text"))