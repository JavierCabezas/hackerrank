class Stack:
    def __init__(self):
        self.instructions = []
        self.stored_word = ''

    def add_instruction(self, instruction_type, parameter):
        if instruction_type == 1: #append
            self.add_to_string(parameter)
            self.instructions.append([1, parameter])
        elif instruction_type == 2:
            deleted_string = self.delete_from_string(int(parameter))
            self.instructions.append([2, deleted_string])
        elif instruction_type == 3:
            self.print_string(int(parameter))
        elif instruction_type == 4:
            self.undo_last_instruction()

    def add_to_string(self, word):
        self.stored_word += word

    def delete_from_string(self, how_many):
        string_to_delete = self.stored_word[(-1) * how_many:]
        self.stored_word = self.stored_word[:(-1) * how_many]
        return string_to_delete

    def print_string(self, position):
        print(self.stored_word[position-1])

    def undo_last_instruction(self):
        ins = self.instructions.pop()
        if ins[0] == 1: #1 is append: Then we should delete
            self.delete_from_string(len(ins[1]))
        elif ins[0] == 2: #2 is delete: Then we should append
            self.add_to_string(ins[1])

s = Stack()
instructions = []
for _ in range(int(input())):
    ins = input().split(" ")
    if len(ins) > 1:
        instructions.append([int(ins[0]), ins[1]])
    else:
        instructions.append([int(ins[0]), 0])

for ins in instructions:
    s.add_instruction(ins[0], ins[1])
