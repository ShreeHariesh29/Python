students = {
    "name" : "shree hariesh",
    "age": 19,
    "Dept" : "Computer Science",
    "clg" : "Jeppiaar Institute of Technology"
}
for x in students:
    print(x)
    
for x in students.values():
    print(x)

for x in students.keys():
    print(x)

for x,y in students.items():
    print(x , y)