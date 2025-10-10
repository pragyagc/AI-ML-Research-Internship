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










#working with csv file
import csv
with open ("data.csv","w",newline="") as file :
 writer = csv.writer(file)
 writer.writerow(["Name", "Age", "City"])
 writer.writerow(["Alice", 25, "Kathmandu"])
 writer.writerow(["Bob", 30, "Pokhara"])

 #reading csv
 import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
