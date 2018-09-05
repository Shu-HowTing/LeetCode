# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
Z字形排列：
    将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
    P   A   H   N
    A P L S I I G
    Y   I   R
    之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"
    输入: s = "PAYPALISHIRING", numRows = 3
    输出: "PAHNAPLSIIGYIR"
    思路：
        不用考虑空格，采用二维数组，然后慢慢填充就行了，一次遍历填充一行中的某一个位置，然后换到下一行
'''
class Solution():
    def convert(self, s_, numRows):
        """
        :type s_: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1):
            return s_
        # 产生一个有numrows单元的list，每个list可以在后面添加元素
        a = [[]for i in range(numRows)]
        r = 0
        direct = 1 # 行前进的方向是向上还是向下
        for c in s_:
            a[r].append(c)
            if r == numRows-1:
                direct = -1
            elif r == 0:
                direct = 1
            r +=direct
        answer = ""
        for x in a:#按行优先打印出来
            for i in x:
                answer += i
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING",4))