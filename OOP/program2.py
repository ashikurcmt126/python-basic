# method
class Student:
    gpa: ""
    roll: ""

    def set_value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = Student()
rahim.set_value(101,3.22)
rahim.display()

Karim = Student()
Karim.set_value(102,3.92)
Karim.display()