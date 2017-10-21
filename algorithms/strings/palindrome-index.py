number_of_testcases = int(input())
words = [input() for _ in range(number_of_testcases)]


def is_palindrome(w):
    return w == w[::-1]

def check_index(w, h, t):
    if is_palindrome(w[:h] + w[(h+1):]):
        return h
    else:
        return t


def check_palindrome(word):
    head = 0
    tail = len(word) -1
    while head < tail:
        if word[head] != word[tail]:
            return check_index(word, head, tail)
        else:
            head += 1
            tail -= 1

    return -1

for word in words:
    print(check_palindrome(word))