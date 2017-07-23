number_of_words = int(input())
words = [ input() for _ in range(number_of_words)]


word_dict = {}
order = len(words)
for word in words:
    if not word in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1

print(len(word_dict))
for word in words:
    if word_dict[word] > 0:
        print(word_dict[word], end=" ")
        word_dict[word] = -1