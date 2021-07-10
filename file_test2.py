fname = input("Enter file name: ")
fh = open(fname)
count = 0.0
add = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    elif  line.startswith("X-DSPAM-Confidence:"):
        count = count +1
        pos = line.find(':')
        add = add + float(line[pos+2:])
avg = add / count
print("Average spam confidence: " + str(avg))
        

 
 

