prices = [7,1,5,3,6,4]

def maximumProfit(prices):
    maxProfit = 0
    L = 0 # L -> Buy
    R = 1 # R -> Sell

    while R < len(prices):

        # when we are making profit
        if prices[R] > prices[L]:
            newProfit = prices[R] - prices[L]
            maxProfit = max(maxProfit, newProfit)
        
        # when we are making loss or no profit
        else:
            L = R
        
        R += 1
    
    return maxProfit

print(maximumProfit(prices))