# -*- coding: utf-8 -*-
# Author: 小狼狗
'''
题目：
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
    给定一个链表: 1->2->3->4->5, 和 n = 2.
    当删除了倒数第二个节点后，链表变为 1->2->3->5.
思路：
    们可以使用两个指针而不是一个指针。第一个指针从列表的开头向前移动 n+1n+1 步，而第二个指针将从列表的开头出发。现在，这两个指针被 nn 个结点分开。我们通过同时移动两个指针向前来保持这个恒定的间隔，直到第一个指针到达最后一个结点。
    此时第二个指针将指向从最后一个结点数起的第 nn 个结点。我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点
'''
# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self._next = None
    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.val)

class Solution:
    def removeNthFromEnd(self, head, n):
        p = head
        q = head
        index = 0
        while index != n:
            p = p._next
            index += 1
        if p == None:
            return head._next
        while p._next != None:
            p = p._next
            q = q._next
        q._next = q._next._next
        return head


class ChainTable(object):
    """链表类，属性包括，链表头： head ； 链表长度： length"""
    def __init__(self, head=Node(None), length=0):
        super(ChainTable, self).__init__()
        self.head = head
        self.length = length

    def isEmpty(self):
        # 判断链表是否为空
        return (self.length == 0)

    def append(self, dataOrNode):
        # 在链表尾部插入Node
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)
        if not self.head:
            self.head = item
            self.length += 1
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

if __name__ == '__main__':
    chain = ChainTable()
    for i in range(10):
        chain.append(i)
    s = Solution()
    head = s.removeNthFromEnd(chain.head,6)
    while head._next:
        head = head._next
        print(head)


