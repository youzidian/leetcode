"""

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

输出中的意思是每一个function之后return的东西
"""

class CQueue:
    def __init__(self):
        self.A = []
        self.B = []
    def appendTail(self, value: int) -> None:
        self.A.append(value)
    def deleteHead(self) -> int:
        print(self.A)
        if self.A == []:
            return -1
        elif self.A !=[]:
            returnNumber = self.A[0]
            self.A.pop(0)
        return returnNumber




# Your CQueue object will be instantiated and called as such:
listA = ["CQueue", "appendTail", "deleteHead", "deleteHead"]
listB = [[], [3], [], []]
obj = CQueue()
for idx, val in enumerate(listA):
    if val == "appendTail":
        obj.appendTail(listA[idx][0])
    elif val == "deleteHead":
        param_2 = obj.deleteHead()
