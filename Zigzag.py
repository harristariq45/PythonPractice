def solution(numbers):

    ans = []
    myset = set(numbers)

    if len(myset) == 1:
        return [0]

    for i in range(len(numbers) - 2):
        if  numbers[i] > numbers[i+1] and numbers[i+1] > numbers[i+2] :
            ans.append(0)

        elif  numbers[i] < numbers[i+1] and numbers[i+1] < numbers[i+2]:
            ans.append(0)

        elif  numbers[i] == numbers[i+1] or numbers[i+1] == numbers[i+2]:
            ans.append(0)

        else:
            ans.append(1)

    return print(ans)


if __name__ == "__main__":
    solution([1, 3, 4, 5, 6, 14, 14])