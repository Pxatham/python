age=int(input("enter your age: "))
if age>=18 and age<=65:
    print("you are eligible for working")
elif age<18:
    print("you are underage ")
else:
    print("you are retired")