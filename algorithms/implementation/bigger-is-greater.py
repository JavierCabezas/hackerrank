def swap_chars(word_list, pos1, pos2):
    temp = word_list[pos1]
    word_list[pos1] = word_list[pos2]
    word_list[pos2] = temp
    return word_list

def reverse_after(word_list, pos):
    word_start = word_list[:pos]
    rest_of_word = word_list[pos:]
    return  word_start + list(reversed(rest_of_word))

def arrange_word(word):
    word_as_list = list(word)
    word_lenght = len(word_as_list)
    if word_lenght < 2:
        return False #Nothing to do here
    for i in range(word_lenght-1):
        is_last_but_one = word_lenght - i  == 2
        next_one_is_bigger = word_as_list[i] < word_as_list[i + 1]
        if next_one_is_bigger and (is_last_but_one or (not is_last_but_one and word_as_list[i+1] > word_as_list[i+2])):
            k = i
            for aux in range(k+1, word_lenght):
                if word_as_list[k] < word_as_list[aux]:
                    j = aux #j is guaranteed to happen (in worst case scenario is k+1)
                    word_as_list = swap_chars(word_as_list, k, j)
                    if k < word_lenght:
                        word_as_list = reverse_after(word_as_list, k+1)
                    return ''.join(word_as_list)

    return False #No maching pair was found

number_of_words = int(input())
words = [input() for _ in range(number_of_words)]

for word in words:
    out = arrange_word(word)
    if out is False:
        print("no answer")
    else:
        print(out)