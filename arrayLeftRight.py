
def solution(numbers, left, right):
    index = 0
    ansArray = []
    leftRightArray = list(range(left, right+1))

    print(leftRightArray)

    for i in range(len(numbers)):
        print(((numbers[i]/(i+1))))
        if ((numbers[i]/(i+1))) in leftRightArray:

            ansArray.append(True)
        else:
            ansArray.append(False)


    return print(ansArray)








if __name__ == "__main__":
    solution([8, 5, 6, 16, 5],1,3)