"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

import defineNodeList as nodeList

class Solution:
    def addTwoNumbers(self, l1, l2):
        listA = []
        listB = []
        l3 =  nodeList.ListNode()
        while l1:
            listA.insert(0,l1.val)
            l1 = l1.next
        while l2:
            # print(l1.val)
            listB.insert(0, l2.val)
            l2 = l2.next

        n1 = int(''.join([str(i) for i in listA]))
        n2 = int(''.join([str(i) for i in listB]))
        total = n1 + n2
        n3 = [int(i) for i in str(total)][::-1]
        for i in str(n3):
            print(i)
            l3.next = i

        print(l3)

        return[int(i) for i in str(total)][::-1]





ListNode_1 = nodeList.ListNode_handle()
l1 = nodeList.ListNode()
# l1_list = [2, 4, 3]
l1_list = [9,9,9,9,9,9,9]
for i in l1_list:
    l1 = ListNode_1.add(i)

ListNode_2 = nodeList.ListNode_handle()
l2 = nodeList.ListNode()
# l2_list = [5, 6, 4]
l2_list = [9,9,9,9]
for i in l2_list:
    l2 = ListNode_2.add(i)



Solution().addTwoNumbers(l1,l2)