# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
单词模式
    给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
    这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式
'''

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern = list(pattern)
        str = str.split(' ')
        if len(pattern) != len(str) or len(set(pattern)) != len(set(str)):
            return False
        dic = {}
        for  x,y in zip(pattern,str):
            if x not in dic:
                dic[x] = y
            y_ = dic.get(x)
            if y != y_:
                return False
        return True

if __name__ == '__main__':
    pattern = input()
    str = input()
    s = Solution()
    print(s.wordPattern(pattern, str))













