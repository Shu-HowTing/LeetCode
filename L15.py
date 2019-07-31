# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
思路：
    它们都要去掉属于同一个组合的排列。通常这样考虑，对于由小到大排好序的数组，构建一棵全排列树，对任意一个组合，第一次出现的全排列必然按照由小到大整整齐齐排列的。
    一旦出现某个元素num小于目前排列res[0..]的最后一个元素res[-1]，则res+[num] 排列必然已经出现了，从而结束对num的处理
'''


class Solution:
    def combinationSum2(self, candidates, target):
        results = []
        candidates.sort() #先排序的目的是为了使空间树好剪枝
        def backtracking(candi, remain, res):
            for c, num in enumerate(candi):
                if c >= 1 and candi[c] == candi[c-1]: #去掉相邻元素相等产生的重复组合
                    continue
                if num == remain:
                    results.append(res+[num])
                    break #直接结束本次循环，因为后面的num肯定比本次大或者一样大
                elif remain < num:
                    break #直接结束本次循环，因为后面的num肯定比本次大或者一样大
                else:
                    backtracking(candi[c+1:], remain - num, res+[num])
        backtracking(candidates, target, [])
        return results


def isSubsetSum(set, n, sum):
    # Base Cases
    if (sum == 0):
        return True
    if (n == 0 and sum != 0):
        return False

    # If last element is greater than
    # sum, then ignore it
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum);

        # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])


N = int(input())
gift_money = list(map(int, input("").split()))
# print(gift_money)
M = int(input())

res = isSubsetSum(gift_money, N, M)
if res:
    print(1)
else:
    print(0)

