nums = [1,2,3,1]

def answer(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return 'true'
    return 'false'

print(answer(nums))

# in this solution -> Time Complexity = O(n^2)