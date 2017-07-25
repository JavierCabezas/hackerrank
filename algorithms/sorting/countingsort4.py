words_dict = {}
biggest_number = 0

def read_input():
    global biggest_number
    for x in range(m):
        temp = input().split() # temp[0] = the integer, temp[1] the string associated
        index_number = int(temp[0])

        #Initialize the dictionary in case it does not exist for this index
        if not index_number in words_dict:
            words_dict[index_number] = []

        #Remove all the words in the first half
        if x < int(m/2):
            temp[1] = '-'

        #Add the data for this specific index number
        words_dict[index_number].append(temp[1])

        #Update the biggest number in case the index is greater
        if index_number > biggest_number:
            biggest_number = index_number

def print_values():
    out = ''
    for x in range(0, biggest_number + 1):
        if x in words_dict:
            out += ' '.join(map(str, words_dict[x])) + ' '
    print(out)


m = int(input())
read_input()
print_values()