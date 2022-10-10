def solution(s):

    for x in s:
        if s.rindex(x) == s.index(x):
            return print(x)

    return "__"


solution("abacabad")
