n = int(input("Size: "))

nums = []
for i in range(n):
    nums.append(int(input("Enter number: ")))

avg = sum(nums) / len(nums)

count = 0
for x in nums:
    if x > avg:
        count += 1

print("Greater than average:", count)