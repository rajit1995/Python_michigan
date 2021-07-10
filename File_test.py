fname = input("Enter file name: ")
print(fname)
fh = open(fname)
print(fh)
for lines in fh :
    ln = lines.rstrip()
    print(ln.upper())
