text = input("Enter sentence: ")

words = text.split()
freq = {}

# loop through words
for i in range(len(words)):
    word = words[i]

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)