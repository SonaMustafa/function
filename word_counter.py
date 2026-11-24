def count_words(text):
    words = text.lower().split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

    return counts


text = input("Mətni daxil edin: ")
result = count_words(text)
print(result)

max_word = ""
max_count = 0

for word in result:
    if result[word] > max_count:
        max_count = result[word]
        max_word = word

print("Ən çox təkrarlanan söz:", max_word)