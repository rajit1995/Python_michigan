fname = input("Enter file name: ")
try :
    fh = open(fname)
    count = 0
    flag=1
except :
    print("File does not exist\n")
    flag = 0 

    
if flag ==1 :
    for line in fh:
        if not line.startswith("From "):
            continue
        elif  line.startswith("From "):
            count = count +1
            spl = line.split()
            print(spl[1])
    print("There were "+str(count)+" lines in the file with From as the first word")



        



        

        
