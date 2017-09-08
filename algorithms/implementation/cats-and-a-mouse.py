from collections import namedtuple
CatMouse = namedtuple('CatMouse', 'cat_a, mouse, cat_b')

number_of_testcases = int(input())
tests = []
for _ in range(number_of_testcases):
    a, b, m = map(int, input().split(" "))
    tests.append(CatMouse(cat_a=a, mouse=m, cat_b=b))


for test in tests:
    dif_a = abs(test.mouse - test.cat_a)
    dif_b = abs(test.mouse - test.cat_b)

    if dif_a == dif_b:
        print("Mouse C")
    elif dif_a < dif_b:
        print("Cat A")
    else:
        print("Cat B")