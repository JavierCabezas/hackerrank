brackets = []
for _ in range(int(input())):
    brackets.append(list(input()))

def get_closing_bracket(bracket):
    if bracket == '(':
        return ')'
    elif bracket =='[':
        return ']'
    elif bracket == '{':
        return '}'

def is_opening_bracket(bracket):
    return bracket in ['(', '{', '[']

def is_matched(bracket_group):
    stack = []
    for bracket in bracket_group:
        if is_opening_bracket(bracket):
            stack.append(bracket)
        else:
            if len(stack) > 0 and bracket == get_closing_bracket(stack[-1]):
                stack.pop()
            else:
                return False

    return len(stack) == 0

for bracket_group in brackets:
    if is_matched(bracket_group):
        print("YES")
    else:
        print("NO")