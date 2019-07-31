# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
最接近的三数之和:
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
    例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
    与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dis = float("inf")
        n = len(nums)
        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if abs(result-target) < dis:
                    dis = abs(result-target)
                    flag = 1 if result-target >=0 else -1
                if result >= target:
                    right -= 1
                if result < target:
                    left += 1
        return dis*flag + target
if __name__ == '__main__':
    s = Solution()
    nums = [-1,2,1,-4]
    target = 2
    print(s.threeSumClosest(nums,target))












