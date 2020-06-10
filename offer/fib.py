"""
面试题10- I. 斐波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。



示例 1：

输入：n = 2
输出：1


In a, b = b, a + b, the expressions on the right hand side are evaluated before being assigned to the left hand side. So it is equivalent to:

c = a + b
a = b
b = c
In the second example, the value of a has already been changed by the time b = a + b is run. Hence, the result is different.


"""

class Solution:

    # 暴力递归方法
    # def fib(self, n):
    #     if n == 0:
    #         print('1', n)
    #         return 0
    #     if n == 1:
    #         return 1
    #     number = self.fib(n-1)+self.fib(n-2)
    #     # print(number)
    #     return number
    #

    # 动态规划 f(n) = f(n-1)+f(n-2)=====>>>f(n+1) = f(n)+f(n-1) 从此而知 可求出 f(n)
    def fib(self, n):
        a, b = 0, 1
        # a = 0
        # b = 1
        for _ in range(n):
            a, b = b, a + b
            # c = a + b
            # a = b
            # b = c
            print(a, b)
        return a % 1000000007

a = Solution()
a.fib(10)