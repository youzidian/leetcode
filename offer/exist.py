"""
面试题12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。



示例 1：

输入：board = [
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]
], word = "ABCCED"
输出：true
示例 2：

输入：board = [
["a","b"],
["c","d"]
], word = "abcd"
输出：false
"""

class Solution:
    def __init__(self, board, word):
        self.board = board
        self.word = board
    def exist(self):
        wordList = [char for char in word]
        for idx, val in enumerate(wordList):
            for key, matrix in enumerate(board):
                if val in matrix and (idx == 0
                                      or val == right
                                      or val == left
                                      or val == down
                                      or val == up):
                    point = matrix.index(val)
                    # print(right)
                    if point == 0 and key == 0:
                        right = matrix[key+1]
                        down = board[key+1][key]
                        print(right, down)
                    elif point != 0:
                        right = matrix[key + 1]
                        down = board[key + 1][key]
                        up = board[key - 1][key]
                        left = matrix[key - 1]
                        print(right, down)
                else:
                    return False
            return True

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# board = [["a","b"],["c","d"]]
# word = "abcd"
a = Solution(board, word)
a.exist()