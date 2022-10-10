def solution(a):
    my_set = set()
    for index, x in enumerate(a):
        setLenBeforeAdd = len(my_set)
        print(index, x)
        print(my_set)
        my_set.add(x)
        if len(my_set) == setLenBeforeAdd:
            return print(x)


if __name__ == "__main__":
    solution([2, 1, 3, 5, 3, 2])
