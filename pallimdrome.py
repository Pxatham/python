n = int(input("How many numbers: "))

nums = []
for i in range(n):
    x = int(input("Enter number: "))
    nums.append(x)

if nums == nums[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")