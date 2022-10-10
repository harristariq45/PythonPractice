
def solution(nums):
    print(nums)
    ans = 0
    x = 0
    y = 0
    for i in range(0,len(nums), 2 ):
        #print(nums[i])
        x += nums[i]

    for z in range(1,len(nums),2):
        #print(nums[i])
        y += nums[z]


    print(y)
    print(x)

    if x >= y:
        return x
    else:
        return y







if __name__ == "__main__":
    solution([1,1,1])
