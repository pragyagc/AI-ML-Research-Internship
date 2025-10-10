file = open("hello.txt", "w")
file.write("Hello, world!\n")
file.write("This is Python file handling.")
file.close()


#for reading the file
file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()


#with automatically closes the filr even if an error occurs
with open("hello.txt", "r") as f:
    content = f.read()
    print(content)

