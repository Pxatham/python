n = int(input("How many numbers: "))

nums = []
for i in range(n):
    nums.append(int(input("Enter number: ")))

sum_pos = 0

for x in nums:
    if x > 0:
        sum_pos = sum_pos + x

print("Sum of positive numbers:", sum_pos)