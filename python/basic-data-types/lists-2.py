number_of_commands = int(input())


class Compiler:
    INSTRUCTION_INSERT = 'insert'
    INSTRUCTION_PRINT = 'print'
    INSTRUCTION_REMOVE = 'remove'
    INSTRUCTION_APPEND = 'append'
    INSTRUCTION_SORT = 'sort'
    INSTRUCTION_POP = 'pop'
    INSTRUCTION_REVERSE = 'reverse'

    INDEX_INSTRUCTION = 0
    INDEX_FIRST_PARAM = 1
    INDEX_SECOND_PARAM = 2

    def __init__(self):
        self.superlist = []


    def parse_command(self, command_as_list):
        instruction = command_as_list[self.INDEX_INSTRUCTION]
        first_param = int(command_as_list[self.INDEX_FIRST_PARAM]) if len(command_as_list) > self.INDEX_FIRST_PARAM else None
        second_param = int(command_as_list[self.INDEX_SECOND_PARAM]) if len(command_as_list) > self.INDEX_SECOND_PARAM else None

        if instruction == self.INSTRUCTION_INSERT:
            self.superlist.insert(first_param, second_param)
        elif instruction == self.INSTRUCTION_PRINT:
            print(self.superlist)
        elif instruction == self.INSTRUCTION_REMOVE:
            self.superlist.remove(first_param)
        elif instruction == self.INSTRUCTION_APPEND:
            self.superlist.append(first_param)
        elif instruction == self.INSTRUCTION_SORT:
            self.superlist.sort()
        elif instruction == self.INSTRUCTION_POP:
            self.superlist.pop()
        elif instruction == self.INSTRUCTION_REVERSE:
            self.superlist.reverse()
        else:
            raise Exception("Not a valid instruction")


compiler = Compiler()
for _ in range(0, number_of_commands):
    command_list = input().split()
    compiler.parse_command(command_list)

