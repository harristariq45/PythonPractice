def maxDifference(px):
    maxDifference1 = -1

    for index in range(len(px)):
        for index1 in range(index+1, len(px)):
            if px[index1]- px[index] > 0 and px[index1]- px[index] > maxDifference1:
                maxDifference1 = px[index1]- px[index]

    return maxDifference1


if __name__ == '__main__':
    maxDifference([7,1,2,5])