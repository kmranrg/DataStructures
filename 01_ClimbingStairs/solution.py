n = int(input('Enter no of steps: '))

def countWays(n):
    one, two = 1, 1
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one

print('Total no of ways =',countWays(n))