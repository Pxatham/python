num = int(input("Enter number: "))

sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div = sum_div + i

if sum_div == num:
    print("Perfect number")
else:
    print("Not perfect number")