"""Buy and Sell Stock – Coding Question

Question:
Given an array prices where prices[i] represents the price of a stock on the i-th day, you can choose one day to buy the stock and a later day to sell it.

Write a Python program to find the maximum profit you can achieve.

If no profit is possible, return 0.

Example 1:

Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5

Explanation:
Buy on day 2 at price 1 and sell on day 5 at price 6.

Profit = 6 - 1 = 5

Example 2:

Input:  prices = [7, 6, 4, 3, 1]
Output: 0

Explanation:
The stock price keeps decreasing, so no profit can be made.

Expected approach: Use a single pass / two-pointer approach with O(n) time complexity and O(1) space complexity."""
def buy_sell_stock(nums):
    profit=0
    minimum=nums[0]
    for i in nums:
        cost=i-minimum
        profit=max(profit,cost)
        minimum=min(minimum,i)
    return profit
print(buy_sell_stock([7, 1, 5, 3, 6, 4]))