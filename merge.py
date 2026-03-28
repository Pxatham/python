n1 = int(input("Enter size of list 1: "))
list1 = []

for i in range(n1):
    list1.append(int(input("Enter number: ")))

n2 = int(input("Enter size of list 2: "))
list2 = []

for i in range(n2):
    list2.append(int(input("Enter number: ")))

merged = []

for x in list1:
    merged.append(x)

for x in list2:
    merged.append(x)

print("Merged list:", merged)