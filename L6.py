# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
三数之和：
    给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0？
    找出所有满足条件且不重复的三元组。

'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_hash = {}
        result = list()
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        if 0 in nums_hash and nums_hash[0] >= 3:
            result.append([0, 0, 0])

        nums = sorted(list(nums_hash.keys()))

        for i, num in enumerate(nums):
            for j in nums[i+1:]:
                if num*2 + j == 0 and nums_hash[num] >= 2:
                    result.append([num, num, j])
                if j*2 + num == 0 and nums_hash[j] >= 2:
                    result.append([j, j, num])

                dif = 0 - num - j
                if dif > j and dif in nums_hash:
                    result.append([num, j, dif])

        return result
if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
