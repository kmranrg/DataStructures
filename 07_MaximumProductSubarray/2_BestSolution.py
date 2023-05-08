nums = [2,3,-2,4]

def solution(nums):
    result = max(nums)
    currentMaximum, currentMinimum = 1, 1

    for i in nums:
        temp = i*currentMaximum
        currentMaximum = max(i*currentMaximum, i*currentMinimum, i)
        currentMinimum = max(temp, i*currentMinimum, i)
        result = max(result, currentMaximum)
    
    return result

print(solution(nums))