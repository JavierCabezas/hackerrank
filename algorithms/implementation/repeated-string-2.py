string_to_repeat = input()
new_string_length = int(input())

times_to_repeat_word = new_string_length // len(string_to_repeat)
remaining_letters = new_string_length % len(string_to_repeat)

number_of_a_in_one_word = string_to_repeat.count("a") * times_to_repeat_word + string_to_repeat[:remaining_letters].count("a")

print(number_of_a_in_one_word)
