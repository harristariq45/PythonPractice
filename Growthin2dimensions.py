import math
import os
import random
import re
import sys


def countMax(upRight):
    array = []
    lenInput = len(upRight)
    #print(lenInput)

    for i in range(lenInput*2):
        print(array)
        array.append(list(map(int, input().rstrip().split())))

    print(array)

if __name__ == '__main__':
    countMax(["1 4", "2 3" , "4 1"])