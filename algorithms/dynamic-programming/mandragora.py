number_of_testcases = int(input())
mandragora_hp = []
for _ in range(number_of_testcases):
    i_dont_need_you = input()
    mandragora_hp.append(list(map(int, input().split(" "))))
    mandragora_hp.sort()

print(mandragora_hp)