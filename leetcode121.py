class Solution:
    def maxProfit(self , prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price< min_price:
                min_price = price
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

    #time: O(n)
    #space: O(1)