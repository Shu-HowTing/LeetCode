# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
两数之和：
    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
    你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用

    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
'''
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 用len()方法取得nums列表长度
    n = len(nums)
    # 创建一个空字典
    d = {}
    for i in range(n):
        a = target - nums[i]
        # 字典d中存在nums[x]时
        if nums[i] in d:
            return d[nums[i]], i
        # 否则往字典增加键/值对
        else:
            d[a] = i

if __name__ == '__main__':
    L = [2,3,2,1]
    print(twoSum(L,4))