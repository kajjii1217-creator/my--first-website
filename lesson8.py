student = {
    "name": "Nishant",
    "age": 20,  
    "city": "Kathmandu",
    "course":"Computer Science"
}

print("name:", student["name"])
print("age:", student["age"])
print("city:", student["city"])
print("course:", student["course"]) 




student["collage"] = "rju"
print("after adding collage", student)
print(student)


print("all details:")
for key , valuse in student.items():
    print(key, ":", valuse)