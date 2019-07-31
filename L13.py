# -*- coding: utf-8 -*-
# Author: 小狼狗
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if prices == None or len(prices) ==0:
            return 0
        Min = prices[0]
        res = 0
        for p in prices:
            res = max(res,p-Min)
            Min = min(Min,p)
        return res
if __name__ == '__main__':
    nums = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit(nums))