student = {
    "first name" : "Ola",
    "last name" : "Nordmann",
    "favourite course" : "Programmering 1"
}
print(f"Studenten heter {student['first name']} {student['last name']}")
if student["favourite course"] == "Programmering 1":
    student["favourite course"] = "ITF10219 Programmering 1"
print(student["favourite course"])
student["age"] = "20"
print(student)