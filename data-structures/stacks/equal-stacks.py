n = int(input())
words = [input() for _ in range(n)]

for word in words:
    start = [letter for index, letter in enumerate(word) if index % 2 == 0]
    end = [letter for index, letter in enumerate(word) if index % 2 == 1]

    print("".join(start) + " " +"".join(end))