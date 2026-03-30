text = input("Enter text: ")

digits = 0
letters = 0
spaces = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
    elif ch == " ":
        spaces += 1

print("Digits:", digits)
print("Letters:", letters)
print("Spaces:", spaces)