# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
最长回文子串
    给定一个字符串,求它的最长回文子串
    思路：
        正反向遍历的方法:遍历字符串，以i为中心点，向前向后一次判断是否相等，相等len+1，时间复杂度将会是O(N^2)
'''
#===================================O(n^2)============================================
class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # insert dollar signs between each character
        s = '$'.join(list(s))
        self.maxlen = 0
        self.retstr = ''
        if len(s) < 2:
            return s
        for i in range(len(s)):
            self.__find_palindrome(s, i, i)
        return ''.join(self.retstr.split('$')).strip()


    def __find_palindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if self.maxlen < k - j + 1:
            self.maxlen = k - j + 1
            self.retstr = s[j + 1:k]


#=====================================O(n)======================================
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        center = 0
        # insert dollar signs between each character
        s = '$' + '$'.join(list(s)) + '$'
        radius_lengths = [1] * len(s)
        for index, _ in enumerate(s):
            if center + radius_lengths[center] > index+radius_lengths[2*center-index]:
                radius_lengths[index] = radius_lengths[2*center-index]
            while index-radius_lengths[index] >= 0 and index+radius_lengths[index] < len(s) and s[index-radius_lengths[index]] == s[index+radius_lengths[index]]:
                radius_lengths[index] += 1
            if radius_lengths[center] < radius_lengths[index]:
                center = index
        pali = s[center-radius_lengths[center]+2:center+radius_lengths[center]:2]
        return pali
if __name__ == '__main__':
    obj = Solution2()
    s = "dbabcbabcbaccbs"
    print(obj.longestPalindrome(s))