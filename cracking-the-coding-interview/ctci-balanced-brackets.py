def is_opening_bracket(item):
    return item == '{' or item == '(' or item =='['

def is_closing_bracked(item):
    return item == '}' or item == ')' or item == ']'

def get_matching_bracket(item):
    if item == '}':
        return '{'
    elif item == ')':
        return '('
    elif item == ']':
        return '['
    else:
        return -1 #To-do: Make a better error

def is_matched(expression):
    stack = []
    for bracket in expression:
        if is_opening_bracket(bracket):
            stack.append(bracket)

        if is_closing_bracked(bracket):
            if len(stack) > 0 and stack[-1] == get_matching_bracket(bracket):
                stack.pop()
            else:
                return False #Parenthesis don't match

    return len(stack) == 0 #If we don't have any remainign elements then the parenthesis are matched

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()


    if is_matched(expression):
        print("YES")
    else:
        print("NO")
