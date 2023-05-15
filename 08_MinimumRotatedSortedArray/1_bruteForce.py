nums = [3,4,5,1,2]

def solution(nums):
    min_num = nums[1]
    for i in nums:
        min_num = min(min_num,i)
    return min_num

print(solution(nums))