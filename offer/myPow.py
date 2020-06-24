"""
面试题16. 数值的整数次方
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。



示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25


解题思路：
快速幂解析（二分法角度）：

x^n=x^(n/2)*x^(n/2) = (x^2)^n/2 令 n/2 为整数，则需要分为奇偶两种情况（设向下取整除法符号为 "////" ）：

当 n为偶数： x^n = (x^2)^(n//2)
当 n 为奇数： x^n = x(x^2)^{n//2}，即会多出一项 x
2^3 =               (2^1)*(2^2)
2^4 = (2^2)*(2^2) = (2^2)^2


x=3 n=5
3^5*(1)>>9^2*(1*3)>>81^1*(1*3)>>6561^0*(1*3*81)
"""

class Solution:
    # def myPow(self, x, n):
    #     if n < 0:
    #         n = n*-1
    #         total = 1/x
    #         x = 1 / x
    #     elif n == 0:
    #         return x
    #     elif x == 0:
    #         return 0
    #     else:
    #         total = x
    #     while n-1:
    #         total = total*x
    #         n -= 1
    #     return total
    #     print(total)

    def myPow(self, x, n):
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        print(res)
        return res


# x = 0.44528
# n = 0


x = 0.00001
n = 2147483647

Solution().myPow(x,n)