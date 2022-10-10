#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    max = sum(arr[len(arr)-4:len(arr)])
    min = sum(arr[0:4])
    print(min,max)


if __name__ == '__main__':

    miniMaxSum([1, 2, 3, 5, 4])