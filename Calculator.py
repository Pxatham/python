class Calculator:
    
    # method to add numbers
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


# create object
c1 = Calculator()

print("Sum:", c1.add(10, 5))
print("Sub:", c1.sub(10, 5))