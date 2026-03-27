text = input("Enter sentence: ")

words = text.split()
unique = []

for i in range(len(words)):
    if words[i] not in unique:
        unique.append(words[i])

result = ""
for word in unique:
    result = result + word + " "

print(result)