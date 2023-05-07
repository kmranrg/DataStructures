nums = [-2,1,-3,4,-1,2,1,-5,4]

def answer(nums):
    maximumSubstringSum = nums[0]
    currentSum = 0

    for i in nums:
        if currentSum < 0:
            currentSum = 0

        currentSum += i
        maximumSubstringSum = max(maximumSubstringSum,currentSum)
    
    return maximumSubstringSum

print(answer(nums))