students = {
    "name" : "shree hariesh",
    "age": 19,
    "Dept" : "Computer Science",
    "clg" : "Jeppiaar Institute of Technology"
}

students.pop("age")
print(students)

del students["clg"]
print(students)

students.popitem()
print(students)