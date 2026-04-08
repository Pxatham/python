# take input
n = int(input("Enter number: "))

original = n
reverse = 0

# reverse number
while n != 0:
    reverse = reverse * 10 + (n % 10)
    n = n // 10

# check palindrome
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")