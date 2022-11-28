def timeToBuy(prices):
    left, right = 0, 1
    maxProfit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            currProfit = prices[right] - prices[left]
            maxProfit = max(maxProfit, currProfit)
        else: 
            left = right 
        right +=1
    return maxProfit

print(timeToBuy([7,1,5,3,6,4]))