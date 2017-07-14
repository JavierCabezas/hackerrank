l = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])

scores = sorted({aux[1] for aux in l})
if len(scores) > 1:
    second_score = scores[1]
    entries = sorted(aux[0] for aux in l if aux[1] == second_score)
    for name in entries:
        print(name)