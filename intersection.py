list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection = []

for x in list1:
    if x in list2 and x not in intersection:
        intersection.append(x)

print("Intersection:", intersection)