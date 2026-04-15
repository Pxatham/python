# parent class
class Animal:
    def speak(self):
        print("Animal makes sound")


# child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")


# object of child class
d = Dog()

d.speak()   # inherited method
d.bark()    # own method