import re
str='100.5小时'
a=re.sub(r'\D','',str)
print(a)