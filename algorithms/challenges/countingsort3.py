def read_input():
    L = []
    for x in range(m):
        temp = input().split() # temp[0] = the integer, temp[1] the string associated (that won't be used in this problem)
        L.append(int(temp[0]))
    return L

def count_and_print(L):
    count = 0
    for temp in range(100):
        count += L.count(temp)
        print(count,end=' ')

m = int(input())
L = read_input()
count_and_print(L)