from typing import List

class BuySellStocks:
    def maxProfit(self, prices: List[int]) -> int:
        #my code
            max_profit = 0 
            curr_profit = 0
            left = 0 
            right = 1
            while right < len(prices):
                if prices[left] > prices[right]:
                    left = right 
                else:
                    curr_profit = prices[right] - prices[left]
                max_profit = max(curr_profit, max_profit)
                right+=1
            return max_profit
        
        
        #Optimised Code : The only difference is that profit is only calculated when prices[left]<prices[right]
        
        # max_profit = 0 
        # curr_profit = 0
        # left = 0 
        # right = 1
        # while right < len(prices):
        #     if prices[left] > prices[right]:
        #         left = right 
        #     else:
        #         curr_profit = prices[right] - prices[left]
        #         max_profit = max(curr_profit, max_profit)
        #     right+=1
        # return max_profit
        
        #Time Complexity: O(n)
        #Space: O(1)
        
        #Window Expansion: The right pointer moves forward (incremented in each iteration) to explore potential selling days.
        # This represents the expansion of the window to include more options for selling.
        
        #Window Adjustment: When the price at left is greater than the price at right, 
        # it means buying on day left and selling on day right would result in a loss. So, to find a potential profit, left is moved to right, 
        # essentially shrinking the window and then immediately expanding it as right moves forward in the next iteration.