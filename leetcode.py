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
        self.val = lst[0]
        r = self
        for item in lst[1:]:
            r.next = ListNode(item)
            r = r.next
        return r.next


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i
            print(dic)


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        result = head
        while l1 != None or l2 != None :
            a = l1.val if l1 != None else 0
            b = l2.val if l2 != None else 0
            summ = a+b+carry
            carry = summ // 10
            summ = summ % 10
            result.next = ListNode(summ)
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            result = result.next
        if carry == 1:
            result.next = ListNode(carry)
        return head.next


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3,3],6))
