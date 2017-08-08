def buildings_to_the_side(h, index, backwards = False):
    number_of_buildings = 0
    i = 0
    if(backwards):
        while index-i >= 0 and h[index-i] >= h[index]:
            number_of_buildings += 1
            i += 1
    else:
        while index+i+1 <= len(h) and h[index+i] >= h[index]:
            number_of_buildings += 1
            i += 1

    return number_of_buildings

def largestRectangle(h):
    if len(h) < 2:
        return h[0]

    max_area = 0
    for current in range(len(h)):
        buildings_to_count = buildings_to_the_side(h, current, True) + buildings_to_the_side(h, current, False) -1
        area = buildings_to_count * h[current]
        if(max_area < area):
            max_area = area

    return max_area


if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h)
    print(result)