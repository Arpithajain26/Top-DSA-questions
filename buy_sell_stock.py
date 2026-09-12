def buy_sell_stock_problem(nums):
    profit=0
    mini=nums[0]
    for i in range(len(nums)):
        cost=nums[i]-mini
        profit=max(profit,cost)
        mini=min(mini,nums[i])
    return profit
print(buy_sell_stock_problem([7,1,5,3,6,4]))