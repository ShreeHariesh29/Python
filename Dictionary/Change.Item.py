students = {
    "name" : "shree hariesh",
    "age": 19,
    "Dept" : "Computer Science",
    "clg" : "Jeppiaar Institute of Technology"
}
print("Old name of the student ",students["name"])
students["name"] = "Shree"
print("Changed name of the student ",students["name"])

# Updating the values
students.update({"age":33})
print("Updated value",students["age"])