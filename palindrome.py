def solution(s):
    if len(s) == 0:
        return ""
    ans = s
    ansLen = 0

    for i in range (len(s)):
        l,r = i,i
        #odd
        while l>=0 and r <len(s) and s[l] == s[r]:
            if (r-l+1)> ansLen:
                print(ans)
                ans = ans.replace(s[l:r + 1],"")
                print(ans)
                ansLen = r-l+1

            l-=1
            r+=1

    #even
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > ansLen:
                ans = ans.replace(s[l:r + 1],"")
                ansLen = r - l + 1

            l -= 1
            r += 1

    ans = solution(ans)

    return ans




if __name__ == "__main__":
    solution("aaacodedoc")