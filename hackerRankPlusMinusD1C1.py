#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p = 0
    z = 0
    n = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            p = p + 1

        elif arr[i] == 0:
            z = z + 1

        elif arr[i] < 0:
            n = n + 1

    print(round(p/len(arr),6))
    print(n/len(arr))
    print(z/len(arr))


if __name__ == '__main__':
    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))

    plusMinus([-4, 3, -9, 0, 4, 1])
