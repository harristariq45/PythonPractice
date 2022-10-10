from itertools import permutations


def Permutations(nums):
    ans = []
    perm = permutations(nums)

    for i in list(perm):
        ans.append(i)

    return print(ans)

if __name__ == "__main__":
    Permutations([1,2,3])