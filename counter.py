n = int(input("How many numbers: "))

nums = []
for i in range(n):
    x = int(input("Enter number: "))
    nums.append(x)

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = 0
most = None

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        most = key

print("Most frequent element:", most)