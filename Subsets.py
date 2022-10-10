from itertools import permutations


def subsets(nums):
    ans = [[]]
    for x in nums:
        ans.append(x)

    perm = permutations(nums)

    for i in perm:
        ans.append(i)

    print(ans)








if __name__ == "__main__":
    subsets([1, 2, 3])