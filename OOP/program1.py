
class Student:
    gpa: ""
    roll: ""

rahim = Student()
#print(isinstance(rahim,Student))
rahim.roll = "101"
rahim.gpa = "3.89"

print(f"Roll: {rahim.roll}, GPA: {rahim.gpa}")

Karim = Student()
Karim.roll = "102"
Karim.gpa = "3.86"

print(f"Roll: {Karim.roll}, GPA: {Karim.gpa}")

