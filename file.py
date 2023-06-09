f=open("hello.txt","w")
f.write("hello world\t")
f.close()

if f:
    print("file successfully")
else:
    print("unsuccessfully:")

f=open("hello.txt","a")
f.write("shubo")
f.close()

f=open("hello.txt","r")
print(f.read())

