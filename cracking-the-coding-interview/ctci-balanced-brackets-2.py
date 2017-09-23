number_of_testcases = int(input())


def is_open_bracket(br):
    return br == '{' or br == '(' or br == '['


def is_match(br_stack, closing_br):
    return closing_br == '}' and br_stack[-1] == '{' or closing_br == ')' and br_stack[-1] == '(' or closing_br == ']' and br_stack[-1] == '['


def is_matched():
    bracket_stack = []
    brackets = input()
    for bracket in brackets:
        if is_open_bracket(bracket):
            bracket_stack.append(bracket)
        else:
            if len(bracket_stack) > 0 and is_match(bracket_stack, bracket):
                bracket_stack.pop()
            else:
                return False

    return len(bracket_stack) == 0


for _ in range(number_of_testcases):
   print("YES" if is_matched() else "NO")