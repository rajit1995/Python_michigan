print("Creating Files\n")
fout = open('output.txt', 'w')
print(fout)
inp = input("Give Your Input : ")
fout.write(inp)
fout.close()
print("\n")
print("\n")
print("\n")
print("Opening File\n ")
fin = open('output.txt', 'r')
for line in fin:
    print(line)
fin.close()
