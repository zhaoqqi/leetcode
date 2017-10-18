# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.getRealNumber(l1)
        num2 = self.getRealNumber(l2)
        return self.getNodeList(num1 + num2)

    def getRealNumber(self, node):
        number = 0
        weight = 1
        while node.next:
            number = number + node.val*weight
            node = node.next
            weight = weight * 10
        number = number + node.val * weight
        return number

    def getNodeList(self, number):
        val = number % 10
        number = number / 10
        first = node = ListNode(val)
        while number:
            node.next = ListNode(number%10)
            node = node.next
            number = number / 10
        return first
