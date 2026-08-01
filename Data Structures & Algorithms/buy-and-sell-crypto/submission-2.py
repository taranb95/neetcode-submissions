class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first = 0
        second = 1
        currsum = 0
        res = 0
        while second < len(prices):
            if prices[first] > prices[second]:
                first = second
            else:
                currsum = prices[second] - prices[first]
                res = max(res,currsum)
            second += 1
        return res
