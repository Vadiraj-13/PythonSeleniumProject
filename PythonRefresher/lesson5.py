class Student:

    def __init__(self, name, rank):
        self._name = name
        self.rank = rank

    def get_details(self):
        print(self._name)
        print(self.rank)


student1 = Student('Ram', 1)
student1.rank = 3
student1.name = "Sham"


class Employee():

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def show_details(self):
        print(self.name)
        print(self.roll_no)


class QA(Employee):
    def __init__(self, dept, name, roll_no):
        super().__init__(name, roll_no)
        self.dept = dept

    def get_dept(self):
        print(self.dept)


class Dev(Employee):
    def __init__(self, dept, name, roll_no):
        super().__init__(name, roll_no)
        self.dept = dept

    def get_dept(self):
        print(self.dept)


emp1 = QA('QA', 'Ram', '1')
emp2 = Dev('Dev', 'Sham', '2')

emp1.show_details()
emp1.get_dept()
