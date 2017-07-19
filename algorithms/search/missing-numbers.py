n = int(input())
A = [int(x) for x in input().split(" ")]
m = int(input())
B = [int(x) for x in input().split(" ")]

#Returns a dict using as keys the value of each of the arrays and as value the number of times that it repeats on that array
def to_dict(arr):
    out = {}
    for a in arr:
        if not a in out:
            out[a] = 0
        out[a] += 1
    return out

def look_for_differences(dict_a, dict_b):
    # We don't check if the array key exists because is given as a constraint
    return [ key for key in dict_a if dict_a[key] != dict_b[key]]

dict_a = to_dict(A)
dict_b = to_dict(B)
differences = look_for_differences(dict_a, dict_b)
print(' '.join(map(str,differences)))