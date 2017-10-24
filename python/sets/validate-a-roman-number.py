valid_roman_words = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
non_repeatable = ['V', 'L', 'D']

last_value = float('Inf')
#Numbers are descending test
def is_valid(roman_words):
    for word in valid_roman_words.keys():
        if not word in valid_roman_words:
            return False

    last_value = 3999
    current_value = valid_roman_words[word]
    if last_value >= current_value:
        last_value = current_value
    else:
        if current_value == 10 or current_value == 5:
            if last_value != 1:
                return False
            else:
                last_value = 0
        elif current_value == 50 or current_value == 100:
            if last_value != 10:
                return False
            else:
                last_value = 9
        elif current_value == 500 or current_value == 1000:
            if last_value != 100:
                return False
            else:
                last_value = 99
        else:
            return False

    #Repetition test
    last_word_frec = {}
    for word in roman_words:
        word_cannot_be_repeated = word in non_repeatable
        if not word in last_word_frec:
            last_word_frec = {}
            last_word_frec[word] = 0
        last_word_frec[word] += 1

        if word_cannot_be_repeated and last_word_frec[word] == 2:
            return False
        else:
            if last_word_frec[word] == 4:
                return False

    return True


roman_words = list(x for x in input())
print(is_valid(roman_words))