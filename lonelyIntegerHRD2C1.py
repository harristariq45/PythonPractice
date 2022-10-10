
def solution(numbers):
    mySet = set(numbers)
    ansArray = 0


    for x in mySet:
        freq =0
        for y in numbers:
            if x == y:
                freq += 1

        if freq == 1:
            ansArray+=x


    return print(ansArray)


if __name__ == "__main__":
    solution([1,2,3,4,3,2,1])
