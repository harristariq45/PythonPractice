def longestCommonPrefix(strs):

    commonPrefix = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return commonPrefix
        commonPrefix += strs[0][i]

    return print(commonPrefix)

if __name__ == "__main__":
    longestCommonPrefix(["flower","flow","flight"])
