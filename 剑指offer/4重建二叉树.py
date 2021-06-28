# 描述
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
# 输入：
# [1,2,3,4,5,6,7],[3,2,4,1,6,5,7]
# 返回值：
# {1,2,5,3,4,6,7}

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        ind = tin.index(pre[0])
        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:ind+1],tin[:ind])
        root.right = self.reConstructBinaryTree(pre[ind+1:],tin[ind+1:])
        return root
    
#     https://blog.csdn.net/xiayiye123/article/details/98204406
# https://blog.csdn.net/Iris_6713/article/details/100824970
# https://blog.csdn.net/qq_18254385/article/details/94596585
