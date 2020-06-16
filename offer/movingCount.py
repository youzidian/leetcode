"""
面试题13. 机器人的运动范围
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
 也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
 但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？



示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
"""

class Solution:
    def __init__(self,m,n,k):
        self.m = m
        self.n = n
        self.k = k
        self.count = 0


    def movingCount(self):
        def dfs(i, j):
            total = sum([int(num) for num in str(i) + str(j)])
            if m <= i or n <= j or k < total or (i, j) in visied:
                return 0
            visied.add((i, j))

            dfs(i + 1, j)
            dfs(i, j + 1)

            self.count += 1
            # print(1 + dfs(i + 1, j) + dfs(i, j + 1))
            # print(1)
            return self.count

        visied = set()
        # why can't define here and modify ?????
        # count = 0
        return dfs(0, 0)


        # def dfs(i, j, si, sj):
        #     if i >= m or j >= n or k < si + sj or (i, j) in visited:
        #         return 0
        #     visited.add((i, j))
        #     return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si,
        #                                                                            sj + 1 if (j + 1) % 10 else sj - 8)
        #
        # visited = set()
        # # print(dfs(0, 0, 0, 0))
        # return dfs(0, 0, 0, 0)






m = 2
n = 3
k = 3
a = Solution(m, n, k)
a.movingCount()