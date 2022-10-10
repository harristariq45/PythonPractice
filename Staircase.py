def solution(n):
    if n == 0:
        return 0

    nArr = [0, 1, 2, 3]
    # print("hiii")
    firstIndex = 2
    secondIndex = 3

    if n > 3:
        for x in range(3,n):
            ans = firstIndex + secondIndex
            nArr.append(ans)
            firstIndex = secondIndex
            secondIndex = ans

    return nArr[n]


if __name__ == "__main__":
    solution(7)
