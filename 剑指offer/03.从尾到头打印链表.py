#常规方法
# 输入一个链表的头节点，按链表从尾到头的顺序返回每个节点的值（用数组返回）。
# 示例1 输入：{1,2,3}
#      返回值：[3,2,1]

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        res=[]
        head=listNode
        while head:
            res.append(head.val)
            head=head.next
        return res[::-1]
       

# 递归
class Solution:
  def __init__(self):
    self.res = []
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
  def printListFromTailToHead(self, listNode):
      # write code here
      if not listNode:
          return self.res
      res = self.printListFromTailToHead(listNode.next)
      res.append(listNode.val)
      return res
