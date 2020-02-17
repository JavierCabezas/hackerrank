number_of_socks = int(input())
pairs = [int(x) for x in input().split()]

sock_dic = {}
number_of_pairs = 0
for pair in pairs:
    if pair not in sock_dic:
        sock_dic[pair] = 0
    sock_dic[pair] += 1

    if sock_dic[pair] == 2:
        del sock_dic[pair]
        number_of_pairs += 1

print(number_of_pairs)