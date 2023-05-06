nums = [2,7,11,15]
target = 9

# let's form a dictionary
prevMap = {} # here the key will be number from nums and value will be it's index

def answer(nums, target):
    for i, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [i, prevMap[diff]]
        prevMap[num] = i
    return

print(answer(nums,target))