Dict = {}
file_name=input("Enter the file name:")
f=open(file_name, "r")
contents=f.readlines()
#print(contents)
for z in contents:
    if(z.endswith("\n")):
        z=z[0:len(z)-1]
    line=z.split(" ")
    #print(line)
    for y in line:
        if y in Dict:
            Dict[y]=Dict[y]+1
        else:
            Dict[y]=1

file_name_dest = input("Enter the destination file name:")
f=open(file_name_dest, "w+")
for i in Dict:
     f.write(i+" : "+str(Dict[i])+"\n")
f.close()
print(Dict)