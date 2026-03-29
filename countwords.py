text = input("Enter sentence: ")

count = 0

for ch in text:
    if ch == " ":
        count += 1

# words = spaces + 1
print("Number of words:", count + 1)