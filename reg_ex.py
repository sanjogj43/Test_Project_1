import re

string = "'I AM NOT YELLING', she said"

new = re.sub('[A-Z]','',string)
print(new)

new = re.sub('[a-zA-Z]','',string)
print(new)

new = re.sub("[.'/,A-Z]","",string)
print(new)