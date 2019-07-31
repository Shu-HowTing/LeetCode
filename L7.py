# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
 回文数:
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
'''
class Solution():
    def is_palindrome(self,x):
        if x<=0 or x%10 == 0:
            return False
        else:
            rev = 0
            while rev < x:
                rev = rev * 10 + x % 10;
                x //= 10;
            return x==rev or x == rev//10
if __name__ == '__main__':
    x = 121
    s = Solution()
    print(s.is_palindrome(x))
