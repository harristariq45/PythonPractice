def solution(nums):

    ranges = []
    while nums:

        start = end = nums.pop(0)
        while nums and nums[0] - end == 1:
            end = nums.pop(0)
        ranges.append(str(start) + ('', '->' + str(end))[start != end])
    return print(ranges)


solution([-1, 0, 1, 2, 6, 7, 9])