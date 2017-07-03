small_difference_indexes = [] #saves the index of the first number of the smallest differences in the array
m = int(input())
nums = list(map(int,input().strip().split()))
nums.sort()
min_dif = nums[1] - nums[0] + 1 #We initialize the difference so we make sure that its changed on the first loop and updated afterwards if needed

for x in range (0, m-2): #The -2 is because we want to get until the second-last element
    dif = nums[x+1] - nums[x]
    if(min_dif > dif):
        min_dif = dif
        small_difference_indexes = [] #Found a new difference: reset the array

    if(min_dif == dif):
        small_difference_indexes.append(x)

for x in small_difference_indexes:
    print(nums[x], end=' ')
    print(nums[x+1], end=' ')
