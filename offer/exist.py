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
        word_list = [char for char in word]
        occupied_dict = {}

        for idx, val in enumerate(word_list):
            for key, matrix in enumerate(board):
                # print('The element: '+val, 'Which list:  '+str(key), matrix)

                if val in matrix and idx == 0:
                    point = matrix.index(val)
                    coordinate = Solution.get_coordinate(self, point, key)
                    # print(coordinate)
                    break

                elif val in matrix and (coordinate.get('right') == str(key) + str(point + 1)
                                        or coordinate.get('down') == str(key + 1) + str(point)):
                    point = matrix.index(val)
                    coordinate = Solution.get_coordinate(self, point, key)
                    break
                # return '1'

    def get_coordinate(self, point, key):
        coordinate_point = {}
        if point == 0 and key == 0:
            coordinate_point['up'] = ''
            coordinate_point['down'] = str(key + 1) + str(point)
            coordinate_point['left'] = ''
            coordinate_point['right'] = str(key) + str(point + 1)
        print(point, key, coordinate_point)
        return coordinate_point


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# board = [["a","b"],["c","d"]]
# word = "abcd"
a = Solution(board, word)
a.exist()