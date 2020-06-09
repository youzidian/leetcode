"""
面试题10- II. 青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
"""

class Solution:
    # 递归暴力
    # def numWays(self,n):
    #     if n == 0:
    #         print('function1', n)
    #         return 0
    #     if n == 1:
    #         print('function2', n)
    #         return 1
    #     print('function3', n)
    #     numberA = self.numWays(n-1)
    #     print('function4', n)
    #     numberB = self.numWays(n-2)
    #     numberSum = numberA+numberB
    #     print(numberSum)
    #     return numberSum

    # 动态分布
    def numWays(self,n):
        a, b = 1,1
        for i in range(n):
            a, b = b, a+b
        # print(a)
        return a

a = Solution()
a.numWays(7)
