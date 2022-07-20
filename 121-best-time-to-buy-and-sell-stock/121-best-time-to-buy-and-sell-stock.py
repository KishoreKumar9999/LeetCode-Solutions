class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxpro = 0
        for i in range(1, len(prices)):
            cur_price = prices[i]
            potential_pro = cur_price - minbuy
            maxpro = max(potential_pro, maxpro)
            minbuy = min(minbuy, cur_price)
            # We will check two things.
            # 1) if this is the minimum buy price 
            # 2) if this is the sell price for max profit
        return maxpro if maxpro>=0 else 0
        