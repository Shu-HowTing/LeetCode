# -*- coding: utf-8 -*-
# Author: 小狼狗

# class Solution:
#     # @param s, a string
#     # @return a list of strings
#     def restoreIpAddresses(self, s):
#         def dfs(s, sub, ips, ip):
#             if sub == 4:                                        # should be 4 parts
#                 if s == '':
#                     ips.append(ip[1:])                          # remove first '.'
#                 return
#             for i in range(1, 4):                               # the three ifs' order cannot be changed!
#                 if i <= len(s):                                 # if i > len(s), s[:i] will make false!!!!
#                     if int(s[:i]) <= 255:
#                         dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
#                     if s[0] == '0': break                       # make sure that res just can be '0.0.0.0' and remove like '00'
#         ips = []
#         dfs(s, 0, ips, '')
#         return ips
# if __name__ == '__main__':
#     S = input()
#     s = Solution()
#     print(len(s.restoreIpAddresses(S)))

# class Solution():
#
#     def validUtf8(self,data):
#         cnt = 0
#         for d in data:
#             if (cnt == 0):
#                 if ((d >> 5) == 0b110):
#                     cnt = 1
#                 elif ((d >> 4) == 0b1110):
#                     cnt = 2
#                 elif ((d >> 3) == 0b11110):
#                     cnt = 3;
#                 elif (d >> 7):
#                     return 0
#             else:
#                 if ((d >> 6) != 0b10):
#                     return 0
#                 cnt-=1
#
#         return 1 if cnt == 0 else 0
# if __name__ == '__main__':
#     N = int(input())
#     data = [int(x) for x in input().split(' ')]
#     s = Solution()
#     print(s.validUtf8(data))
#
# class Solution():
#
#     def validUtf8(self,data):
#         count = 0
#         for val in data:
#             if not count:
#                 if((val>>5)==0b110):
#                     count = 1
#                 elif((val>>4)==0b1110):
#                     count = 2
#                 elif((val>>3)==0b11110):
#                     count = 3
#                 elif(val>>7):
#                     return 0
#                 continue
#             if((val>>6)!=0b10):
#                 return 0
#             count-=1
#
#         return 1


# def find_1(rect1,M):
# #     global rect
# #     rect = rect1
# #     # 遍历矩阵找1,块的定位
# #     count = 0
# #     for  i in range(M):
# #         for j in range(M):
# #             # 当找到1时,开始处理其所在的块
# #             if (rect1[i][j] == 1):
# #                 block(i, j, M)
# #                 count += 1
# #
# #     return count
# #
# # # 判断连续块,递归
# # def block(i,j,M):
# # 		# 修改(i,j)坐标对应的数组元素的值(避免递归时反复判断相邻元素)
# # 		rect[i][j] = 4
# # 		# 分别判断上下左右
# # 		if (i < M - 1 and rect[i + 1][j] == 1):
# # 			block(i + 1, j, M);
# # 		if (i > 0 and rect[i - 1][j] == 1):
# # 			block(i - 1, j, M)
# # 		if (j < M - 1 and rect[i][j + 1] == 1):
# # 			block(i, j + 1,M);
# # 		if (j > 0 and rect[i][j - 1] == 1):
# # 			block(i, j - 1, M);
# # if __name__ == '__main__':
# #     N = int(input())
# #     array = []
# #     for i in range(N):
# #         array.append([int(x) for x in input().split(' ')])
# #     print(find_1(array,N))



#
# def Fac(N):
#     size = 1000
#     L = [0 for i in range(size)]
#     L[0] = 1
#     flag = 1
#     carray = 0
#     for i in range(2,N+1):
#         for j in range(1,flag+1):
#             temp = L[j-1] * i + carray
#             L[j-1] = temp % 10
#             carray = temp // 10
#         while carray:
#             flag += 1
#             L[flag-1] = carray % 10
#             carray = carray // 10
#     return L
# def Factorial(num):
#     size = 1000
#     array = [0 for x in range(size)]
#     array[0] = 1
#     for i in range(2,num+1):
#         carry = 0
#         for j in range(size):
#             temp = array[j]*i+carry
#             array[j] = temp%10
#             carry = temp//10
#     return array
# n = int(input())
# print(Fac(n))
# print(Factorial(n))
#
# s =1
# for i in range(1,n+1):
#     s *= i
# print(s)


