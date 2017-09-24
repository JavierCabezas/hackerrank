class TrieNode:
    def __init__(self):
        self.sons = {}
        self.complete_words = 0
        #self.is_word = False
trie = TrieNode()


def add_word_to_trie(word_to_add):
    current = trie
    for letter in word_to_add:
        if not letter in current.sons:
            current.sons[letter] = TrieNode()
        current = current.sons[letter]
        current.complete_words += 1
    #current.is_word = True


def find(word_to_find):
    current = trie

    for letter in word_to_find:
        if letter in current.sons:
            current = current.sons[letter]
        else:
            return 0

    return current.complete_words

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
