nums = [1,2,3,1]

def answer(nums):
    memory = []
    for i in nums:
        if i in memory:
            return 'true'
        memory.append(i)
    return 'false'

print(answer(nums))

# in this solution -> Time Complexity = O(n), however we are using memory of O(n)
# but still it's the best possible solution