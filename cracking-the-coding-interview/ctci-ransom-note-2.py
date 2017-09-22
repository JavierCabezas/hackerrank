def ransom_note(magazine, ransom):
    word_dict = {}
    for word in magazine:
        if not word in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1

    for word in ransom:
        if not word in word_dict or word_dict[word] == 0:
            return False
        else:
            word_dict[word] -= 1

    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
print("Yes" if answer else "No")


