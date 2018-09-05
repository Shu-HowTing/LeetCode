# -*- coding: utf-8 -*-
# Author: 小狼狗
# import math
# def calc_ent(x):
#     """
#         calculate shanno ent of x
#     """
#     x_value_list = set(x)
#     ent = 0.0
#     for x_value in x_value_list:
#         count = 0
#         for i in x:
#             if i==x_value:
#                 count += 1
#         p = count/len(x)
#         logp = math.log2(p)
#         ent -= p * logp
#     return ent
#
# def calc_condition_ent(x, y):
#     """
#         calculate ent H(y|x)
#     """
#
#     # calc ent(y|x)
#     x_value_list = set(x)
#     ent = 0.0
#     for x_value in x_value_list:
#         sub_y = []
#         for i,value in enumerate(x):
#             if i == x_value:
#                 sub_y.append(y[i])
#         temp_ent = calc_ent(sub_y)
#         ent += (float(len(sub_y)) /n) * temp_ent
#
#     return ent
#
# def calc_ent_grap(x,y):
#     """
#         calculate ent grap
#     """
#
#     base_ent = calc_ent(y)
#     condition_ent = calc_condition_ent(x, y)
#     ent_grap = base_ent - condition_ent
#
#     return ent_grap
#
# if __name__ == '__main__':
#     n = int(input())
#     L = []
#     for i in range(n):
#         L.append([int(x) for x in input().split(',')])
#     x = [x[0] for x in L]
#     y = [x[1] for x in L]
#     print("{:.2f}".format(calc_ent_grap(x, y)))






