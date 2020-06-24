"""
面试题17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

"""

class Solution:
    # def printNUmbers(self,n):
    #
    #     list_a = []
    #     i = 1
    #     while i:
    #         if len(str(i)) > n:
    #             break
    #         list_a.append(i)
    #         i += 1
    #     print(list_a)
    #     return list_a

    def printNUmbers(self, n):
        max_number = ''
        while n:
            max_number = max_number+'9'
            n -= 1
        list_a = list(range(1, int(max_number)+1))
        print(list_a)
        return list_a
n = 3
Solution().printNUmbers(n)
