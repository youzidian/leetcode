"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

"""

class Solution:
    def __init__(self,s):
        self.s = s
    def replaceSpace(self):
        # print(123)
        string = s.replace(' ','%20')
        return string

s = "We are happy."
a = Solution(s)
a.replaceSpace()