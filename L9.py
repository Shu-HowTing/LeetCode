# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
不同路径：
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
    问总共有多少条不同的路径？
'''
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for i in range(m)]for j in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[j][i] = dp[j][i-1]+dp[j-1][i]
        return dp[n-1][m-1]
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7,3))



