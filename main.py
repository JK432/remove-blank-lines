# Develop a python code to read a text file, copy the contents to another file after removing the blank lines. 
f1=open("file1.txt","r")
f2=open("file2.txt","w")
f2.write("kdfsl")
M=f1.read()
L=""
for i in M:
  if(i!="\n"):
     L= L+i

f2.write(L)