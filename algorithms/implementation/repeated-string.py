string_to_check = input()
repeat_this_many_times = int(input())


def repeats_at_start(word, number_of_repetitions):
    return word.count("a") * number_of_repetitions


def repeats_at_end(word, number_of_characters):
    return word[:number_of_characters].count("a")


number_of_repetitions = repeat_this_many_times // len(string_to_check)
last_characters = repeat_this_many_times - number_of_repetitions * len(string_to_check)

print(
    repeats_at_start(string_to_check, number_of_repetitions) +
    repeats_at_end(string_to_check, last_characters)
)