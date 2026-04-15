# define a class
class Student:
    
    # constructor (runs automatically)
    def __init__(self, name, marks):
        self.name = name      # instance variable
        self.marks = marks

    # method to display data
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


# create object
s1 = Student("Pratham", 85)

# call method
s1.display()