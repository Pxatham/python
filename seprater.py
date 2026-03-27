# number of elements
n = int(input("How many numbers: "))

nums = []
for i in range(n):
    x = int(input("Enter number: "))
    nums.append(x)

result = {"even": [], "odd": []}

for num in nums:
    if num % 2 == 0:
        result["even"].append(num)
    else:
        result["odd"].append(num)

print(result)