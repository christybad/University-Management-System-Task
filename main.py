class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return('name: ' + self.name + '\nage: ' + self.age + '\ngender: ' + self.gender)

personn = Person('Christy','17','F')
print(Person.get_details(personn))


class Student(Person):
    def __init__(self,name,age,gender,student_id,course):
        super().__init__(name,age,gender)
        self.student_id = student_id
        self.course = course
        self.grades = []
        self.average = 0
       

    def set_student_details(self,student_id, course):
        self.student_id = student_id
        self.course = course

    def add_grade(self,grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if len(self.grades) > 0:
            average = sum(self.grades)/len(self.grades)
            return(average)
        else:
            return(0)
        
    def get_student_summary(self,name,age,gender,student_id,course):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.student_id)
        print(self.course)
       


student1 = ('fathima','17','F','1234','history')

Student.add_grade(student1,8)
Student.add_grade(student1,6)
Student.add_grade(student1,7)

Student.calculate_average_grade(student1)
print(Student.get_student_summary(student1))