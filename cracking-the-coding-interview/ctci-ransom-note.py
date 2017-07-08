def check_if_ransom_is_in_magazine(dict, ransom):
    for word in ransom:
        if not word in dict: #If we don't have the word in the dictioary then we can't write it
            return False
        dict[word] -= 1 #We substract one word from the dictionary.

        if dict[word] < 0: #If we "used" a word that we didn't have we can't write the letter and we need to buy new magazines
            return False

    return True #We wrote the complete letter and we can succesfully do our crime, congratulations! :D


def ransom_note(magazine, ransom):
    magazine_dict = {}
    for word in magazine:
        if not word in magazine_dict:
            magazine_dict[word] = 0 #Iniatilize the dictionary with zeroes

        magazine_dict[word] += 1 #Add one for every word we get

    return check_if_ransom_is_in_magazine(magazine_dict, ransom)


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')

if (ransom_note(magazine, ransom)):
    print("Yes")
else:
    print("No")