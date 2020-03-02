def has_letter_in_common(first_word, second_word):
    word_dictionary = {}

    for letter in first_word:
        if letter not in word_dictionary:
            word_dictionary[letter] = True

    for letter in second_word:
        if letter in word_dictionary:
            return True

    return False


number_of_word_pairs = int(input())
for _ in range(number_of_word_pairs):
    first_word, second_world = input(), input()
    print("YES" if has_letter_in_common(first_word, second_world) else "NO")
