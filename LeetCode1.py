
def maxProfit():
    prices = [7, 1, 5, 10, 6, 4]

    highest = 0
    HIndex = 0
    lowest = 0


    for index, x in enumerate(prices):
        print(index,x)
        if (x > highest):
            highest = x
            HIndex = index

    print("--------------------------------------------")

    lowest = highest
    for index, x in enumerate(prices[HIndex:]):
        print(index,x)
        if (x < lowest):
            lowest = x


    print(highest)
    print(lowest)
    print(highest-lowest)



    #profit = highest - lowest




if __name__ == "__main__":
    maxProfit()
    