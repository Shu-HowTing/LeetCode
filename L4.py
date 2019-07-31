# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
反转整数:
    给定一个 32 位有符号整数，将整数中的数字进行反转
'''

class Solution():
    def reverse(self,x):
        rev = 0
        flag = 1 if x>0 else -1
        x = abs(x)
        while x != 0:
            res = x % 10
            x //= 10
            rev = rev * 10 + res
        return flag*rev
if __name__ == '__main__':
    x = int(input())
    s = Solution()
    print(s.reverse(x))



















