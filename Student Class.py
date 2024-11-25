class student:
    Grade= 7
    def __init__(self, name, age):
        self.name=name
        self.age=age



ob1 = student("Mike","14")
ob2 = student("Sunandan","15")
ob3= student("Charles","13")
print(ob1.name,ob1.age,ob1.Grade)