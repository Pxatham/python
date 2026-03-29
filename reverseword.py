sentence = input("Enter sentence: ")

words = sentence.split()
result = ""

for word in words:
    rev = ""
    for ch in word:
        rev = ch + rev
    result = result + rev + " "

print("Output:", result)