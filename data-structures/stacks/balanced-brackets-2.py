iterations = int(input())


class ParenthesisChecker:
    OPEN_PAREN = ['{', '[', '(']
    paren_stack = []

    def manage_parenthesis(self, parenthesis):
        if parenthesis in self.OPEN_PAREN:
            self.paren_stack.append(parenthesis)
            return True
        else:
            if self.is_closing_parenthesis(parenthesis):
                self.paren_stack.pop()
                return True
            else:
                return False

    def is_closing_parenthesis(self, candidate):
        if len(self.paren_stack) == 0:
            return False

        return candidate == ']' and self.paren_stack[-1] == '[' or \
               candidate == '}' and self.paren_stack[-1] == '{' or \
               candidate == ')' and self.paren_stack[-1] == '('

    def is_balanced(self, parenthesis_string):
        self.paren_stack = []
        for parenthesis in parenthesis_string:
            if not self.manage_parenthesis(parenthesis):
                return False

        return len(self.paren_stack) == 0


paren_class = ParenthesisChecker()
for _ in range(0, iterations):
    candidate = input()
    print("YES" if paren_class.is_balanced(candidate) else "NO")
