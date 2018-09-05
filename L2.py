# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
最长不重复子串
    Given "abcabcbb", the answer is "abc", which the length is 3.
    思路:
        用一个hashmap来记录每一个元素最近一次出现的index
        维护两个指针，一个start指向当前元素上一次出现的位置，还有一个用来遍历整个str，时间复杂度O(n)
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        used_Char = {}

        for i in range(len(s)):
            if s[i] in used_Char and start <= used_Char[s[i]]:
                start = used_Char[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            used_Char[s[i]] = i
        return maxLength

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abca"))