import re
fh=open('example.txt')
x=re.findall('[0-9]+',fh)
print(x)    
