
def twoSum(nums, target):


    ans = []
    for index1,x in enumerate(nums):
        print("x = ", x)
        for index2,y in enumerate(nums[1:]):
            print("y = ", y)
            if x + y == target:
                if index1 != index2+1:
                    ans.append(index1)
                    ans.append(index2+1)
                    return print(ans)


    return 0


if __name__ == "__main__":
    twoSum([2,5,5,11], 10)
