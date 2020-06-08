"""
面试题06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。



示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
"""



class Solution:
    def __init__(self, head):
        self.head = head
    # def reversePrint(self):
    #     count = 0
    #     nums = []
    #     nums2 = []
    #     # print(head)
    #     while self.head:
    #         count += 1
    #         nums.append(self.head.val)
    #         head = head.next
    #     while count:
    #         count -= 1
    #         nums2.append(nums[count])
    #     return nums2


    def reversePrint(self):
        nums = []
        for i in reversed(head):
            nums.append(i)
        return nums

    def reversePrint(self):
        # print(head[1])
        count = len(head)
        nums = []
        while count>0:
            count -= 1
            # print(head[count])
            nums.append(head[count])
        return nums


head = [1, 3, 2]
a = Solution(head)
a.reversePrint()


