n = int(input("How many elements: "))

nums = []
for i in range(n):
    nums.append(int(input("Enter number: ")))

result = []

# add non-zero
for x in nums:
    if x != 0:
        result.append(x)

# add zeros
for x in nums:
    if x == 0:
        result.append(x)

print(result)