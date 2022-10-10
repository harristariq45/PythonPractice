def lastStoneWeight(weights):
    while sum(weights) > 0 or len(weights) > 1:

        weights.sort(reverse=True)
        stone1 = weights[0]
        stone2 = weights[1]

        if len(weights) > 1:
            weights.pop(1)

        if len(weights) > 0:
            weights.pop(0)

        if stone1 == stone2:
            stone1 = 0
            stone2 = 0

        if stone1 < stone2:
            stone1 = 0
            stone2 = stone2 - stone1

        if stone1 > stone2:
            stone1 = stone1 - stone2
            stone2 = 0

        if stone1 > 0:
            weights.append(stone1)

        if stone2 > 0:
            weights.append(stone2)

    print("sum", sum(weights))
    return sum(weights)


if __name__ == '__main__':
    lastStoneWeight([4,3,2,4,5])
