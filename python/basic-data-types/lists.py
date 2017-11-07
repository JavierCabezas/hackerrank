l = []
for _ in range(int(input())):
    s = input().split()
    command, arguments = s[0], s[1:]
    if command == "print":
        print(l)
    else:
        command += "("+ ",".join(arguments) +")"
        eval("l."+command)