a=int(input("enter value 1 "))
b=int(input("enter value 2 "))
c=int(input('''
1 = +
2 = *
3 = /
4 = -
enter your choice '''))
if (c==1):
    print(a+b)
elif (c==2):
    print(a*b)
elif (c==3):
    print(a/b)
elif (c==4):
    if a>b:
        print(a-b)
    else:
        print(b-a)
else:
    print("wrong choice")
