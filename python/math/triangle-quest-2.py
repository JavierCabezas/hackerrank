for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    first_number = sum(list(1 * 10**position for position in range(i)))
    print(first_number**2)