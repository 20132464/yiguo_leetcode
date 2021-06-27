# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# [
#   [1,2,8,9],
#   [2,4,9,12],
#   [4,7,10,13],
#   [6,8,11,15]
# ]
# 给定 target = 7，返回 true。

# 给定 target = 3，返回 false。



# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array:
            return False
        m = len(array)
        n = len(array[0])
        a, b = 0, n-1
        while a<m and b>=0:
            if array[a][b] == target:
                return True
            elif array[a][b] < target:
                a += 1
            else:
                b -= 1
        return False
