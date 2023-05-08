nums = [2,3,-2,4]

def result(nums):
    multiplyResult = []
    for i in range(len(nums)):
        currentMultiplication = nums[i]
        for j in range(i+1,len(nums)):
            currentMultiplication *= nums[j]
            multiplyResult.append(currentMultiplication)
            print("i",nums[i])
            print("j",nums[j])
            print("currentMultiplication",currentMultiplication)
            print('multiplyResult',multiplyResult)
    return max(multiplyResult)

print(result(nums))