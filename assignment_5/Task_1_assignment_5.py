students = {
    "Robin" : 90,
    "Alice" : 85,
    "krish" : 80
}

name = input("Enter the student's name: ")

if students.get(name)!=None: 
    marks = students.get(name)
    print(f"{name}'s marks: {marks}")
else:
    print("Student not found.")