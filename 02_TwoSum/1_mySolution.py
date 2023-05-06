import itertools

nums = [3,3]
target = 6

all_combinations = itertools.combinations(nums,2)
output = []

for i in all_combinations:
    print(i)
    if sum(i) == target: # as per the given constraint in the question, there will be only one feasible pair
        if i[0] != i[1]:
            output.append(nums.index(i[0]))
            output.append(nums.index(i[1]))
        else:
            output.append(nums.index(i[0]))
            output.append(nums.index(i[1],nums.index(i[0])+1))

print(output)