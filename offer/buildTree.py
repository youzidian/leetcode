"""

面试题07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。



例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

四种主要的遍历思想为：

前序遍历：根结点 ---> 左子树 ---> 右子树

中序遍历：左子树---> 根结点 ---> 右子树

后序遍历：左子树 ---> 右子树 ---> 根结点

层次遍历：只需按层次遍历即可

首先，明确一点，无论是前序，中序，后序，遍历都是从左至右。然后我们需要将每个树看成独立的最小单元二叉树。比如 d,e、fg、bdf、abc。


首先，这些边界是用来“递归子树”的，递归某子树时，需要传入此子树的三个参数：此子树根节点在先序遍历中的索引
pre_root 、此子树在中序遍历列表中的区间（即左 / 右边界 in_left 和 in_right） 。
为找到左、右子树在中序遍历中的边界，我们需要首先找到此树的根节点在中序遍历中的索引 i （就是代码中在HashMap中搜索到的 i ）；
通过索引 i ，我们可以把此树的中序遍历区间劈成三部分：此树的左子树区间、此树的根节点、此树的右子树区间。
最后，左子树区间 和 右子树区间 有对应的 左/右边界 in_left 和 in_right ，分别用于递归左子树和右子树；对应以下代码：

root.left = self.recur(pre_root + 1, in_left, i - 1) # 开启左子树的下层递归
root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right) # 开启右子树的下层递归
具体看左子树和右子树的 左 / 右边界：

`i` 为此树的根节点在中序遍历中的索引

"此树的左子树"的左边界 等于 "此树"的左边界 `in_left`
"此树的左子树"的右边界 等于 `i - 1` （被 `i` 劈成三部分）

"此树的右子树"的左边界 等于 `i + 1` （被 `i` 劈成三部分）
"此树的右子树"的右边界 等于 "此树"的右边界 `in_right`
"""
from binarytree import Node

class Solution:

    def __init__(self,preOrder,inOrder,count):
        self.preOrder = preOrder
        self.inOrder = inOrder
        self.count=count

    def buildTree(self):
        self.dic = {}
        self.po = self.preOrder
        # print(range(len(preOrder)))
        for i in range(len(self.preOrder)):
            self.dic[inOrder[i]] = i
        # print(self.dic)
        return self.recur(0, 0, len(inOrder)-1)

    def recur(self,pre_root,in_left,in_right):
        # print(pre_root,in_left,in_right)
        if in_left > in_right:
            # self.count += 1
            return None  # 终止条件：中序遍历为空
        # print(123)
        root = Node(self.po[pre_root])  # 建立当前子树的根节点
        i = self.dic[self.po[pre_root]]  # 搜索根节点在中序遍历中的索引，从而可对根节点、左子树、右子树完成划分。
        # print(self.po[pre_root],pre_root)
        # print(i,pre_root)
        self.count+=1
        print(self.count)
        root.left = self.recur(pre_root + 1, in_left, i - 1)  # 开启左子树的下层递归 in_left 和 in_right 是中序排列的区间
        root.right = self.recur(i - in_left + pre_root + 1, i + 1, in_right)  # 开启右子树的下层递归
        # print(self.count,root)
        print(root)
        return root  # 返回根节点，作为上层递归的左（右）子节点



    # def recursion(self):

pre = [3, 9, 20, 15, 7]
inOrder = [9, 3, 15, 20, 7]
count = 0
a = Solution(pre, inOrder,count)
a.buildTree()