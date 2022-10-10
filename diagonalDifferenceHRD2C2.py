def diagonalDifference(arr):
    arrSize = len(arr)

    # left to right
    left_to_right = 0 # adder
    i = 0
    exit = True

    while exit:
        left_to_right += arr[i][i]
        i += 1
        if i == arrSize:
            exit = False


    #right to left
    right_to_Left = 0
    i = 0
    j = arrSize-1
    exit = True

    while exit:
        right_to_Left += arr[i][j]
        i += 1
        j -= 1
        if i == arrSize:
            exit = False

    return abs(left_to_right-right_to_Left)






diagonalDifference([[11, 2, 4],
                    [4, 5, 6],
                    [10, 8, -12]])