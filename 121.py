class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = -float('inf')

        for element in prices:
            if element < min_price:
                min_price = element
            if element - min_price >= max_profit:
                max_profit = element - min_price
        
        return max_profit

        return 0
        