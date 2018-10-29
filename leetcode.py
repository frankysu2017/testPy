#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

    def printList(self):
        temp = self
        while temp:
            print(temp.val, end='->')
            temp = temp.next
        print(None)

    def createList(self, lst):
        r = self
        for item in lst:
            r.next = ListNode(item)
            r = r.next
        return r.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        while l1 != None or l2 != None :
            a = l1.val if l1 != None else 0
            b = l2.val if l2 != None else 0
            summ = a+b+carry
            carry = summ // 10
            summ = summ % 10
            result = ListNode(summ)
            l1 = l1.next if l1.next != None else None
            l2 = l2.next if l2.next != None else None
            result = result.next
        if carry == 1:
            result = ListNode(carry)
        return result


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l1.printList()
    l2.printList()

    l3 = ListNode()
    l3.createList([1,2,3,4])
    l3.printList()

    s = Solution()
    print(s.addTwoNumbers(l1=l1, l2=l2))