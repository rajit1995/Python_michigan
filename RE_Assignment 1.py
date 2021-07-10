import re
fname = input('Enter your file name : ')
handle = open(fname)
lst = list()
add = 0
for line in handle:
    y= re.findall('[0-9]+',line)
    if len(y) == 0 :
        continue
    else:
        lst = lst + y
for word in lst:
    add = add + int(word)
print(add)
    
    
