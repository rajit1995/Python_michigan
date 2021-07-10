fnam = input("Enter file name : ")
fh = open(fnam)
lst = list()
for line in fh:
    spl = line.split()
    count = len(spl)
    for val in range (len(spl)):
        if spl[val] in lst :
            continue
        else :
            lst.append(spl[val])
lst.sort()
print(lst)
            
