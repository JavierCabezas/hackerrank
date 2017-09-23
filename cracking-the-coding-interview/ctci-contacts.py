
trie = {}
END_WORD = '*'


def add_word_to_trie(word_to_add):
    current = trie
    for letter in word_to_add + END_WORD:
        if not letter in current:
            current[letter] = {}
        current = current[letter]


def number_of_complete_words(current):
    if current is None:
        return 0

    total = 0
    for letter in current.keys():
        if letter == END_WORD:
            total += 1
        else:
            return total + number_of_complete_words(current[letter])
    return total


def find(word_to_find):
    current = trie
    for letter in word_to_find:
        if letter in current:
            current = current[letter]
        else:
            return 0

    return number_of_complete_words(current)

n_operations = int(input())
to_do = []
for idx in range(n_operations):
    to_do.append({})
    to_do[idx]['instruction'], to_do[idx]['word'] = input().split(" ")

for op in to_do:
    if op['instruction'] == 'add':
        add_word_to_trie(op['word'])
    elif op['instruction'] == 'find':
        print(find(op['word']))
