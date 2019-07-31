# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
依次给出n个正整数A1，A2，… ，An，将这n个数分割成m段，每一段内的所有数的和记为这一段的权重，
m段权重的最大值记为本次分割的权重。问所有分割方案中分割权重的最小值是多少？
思路：
    问题分析：二分查找（Binary Search）
    1、所给的数子都是正整数（很重要）。
    2、让求的解可以事先确定其的范围[sum(nums) / m，sum(nums)]：
        A: 最优解一定不小于sum(nums) / m，这个很好证明（前提，都是非负数），一个序列nums 被分割m段，如果有一个段小于sum(nums) / m，那么其他子段一定有一个大于平均值数，所以此次分割的分数最小一定是sum(nums) / m。
        B: 其次是，最优解一定不大于sum(nums)，这个很好理解，因为无论它如何分割，子段的最大值不会超过这个序列的总和。
    3、由2可知，我们已经知道解的范围，现在只要枚举这些值，选择最优解即可。所以可以使用二分查找，以确定那个值是最优解。
'''
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        size = len(nums)
        high = sum(nums)
        low = high // m
        while low <= high:
            mid = (low + high) // 2
            n = m
            cnt = 0
            valid = True
            for x in range(size):
                if nums[x] > mid:
                    valid = False
                    break
                if cnt + nums[x] > mid:
                    n -= 1
                    cnt = 0
                cnt += nums[x]
                if n == 0:
                    valid = False
                    break
            if valid:
                high = mid - 1
            else:
                low = mid + 1
        return low

if __name__ == '__main__':
    s = Solution()
    n,m = [int(x) for x in input().split(' ')]
    nums = [int(x) for x in input().split(' ') ]
    if n<m:
        print(False)
    else:
        print(s.splitArray(nums, m))

