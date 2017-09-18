from collections import deque
d = deque()

for _ in range(int(input())):
    temp = input()
    try:
        ins, value = temp.split()
    except:
        ins = temp
        value = None

    if ins == 'append':
        d.append(value)
    elif ins == 'pop':
        d.pop()
    elif ins == 'popleft':
        d.popleft()
    elif ins == 'appendleft':
        d.appendleft(value)

print(*d, end=' ')