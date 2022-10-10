import math


def twoSum(s):
    ans = ""
    romanHashMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    res = 0

    for i in range(len(s)):
        if i+1 < len(s) and romanHashMap[s[i]] < romanHashMap[s[i+1]]:
            res -= romanHashMap[s[i]]
        else:
            res += romanHashMap[s[i]]

    return print(res)


if __name__ == "__main__":
    twoSum("MCMXCIV")