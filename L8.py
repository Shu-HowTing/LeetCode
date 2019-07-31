# -*- coding: utf-8 -*-
# Author: 小狼狗

'''
盛最多水的容器:
    给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
'''
# 暴力(O(n^2))
class Solution1():
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = min(height[i],height[j])*(j-i)
                if area > max:
                    max = area
        return max

# 双指针
class Solution2():
    def maxArea(self, height):
        max_area = 0
        i = 0
        j = len(height)-1
        while i < j:
            area = min(height[i],height[j])*(j-i)
            max_area = max(max_area,area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

if __name__ == '__main__':
    L = [1,8,6,2,5,4,8,3,7]
    s = Solution2()
    print(s.maxArea(L))