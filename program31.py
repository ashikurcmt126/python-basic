
file1 = open("student.txt","r+") #r+ means read write access both
#text = file1.read()
#print(text)

#size = len(text)
#print(size)

for line in file1:
    print(line)

file1.close()
