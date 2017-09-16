def wrapper(original_function):
    def format_phone(list_of_phones):
        new_list_of_phones = ["+91 "+c[-10:-5]+" "+c[-5:] for c in list_of_phones]
        return original_function(new_list_of_phones)

    return format_phone

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)