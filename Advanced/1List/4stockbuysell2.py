def maxProfit(price,n):
    profit=0
    for i in range(1,n):
        if price[i]>price[i-1]:
            profit+=price[i]-price[i-1]
    return profit

print(maxProfit([1,5,3,1,2,8],6))       