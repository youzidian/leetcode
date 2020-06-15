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
        self.word_list = [char for char in word]

    def exist(self):
        def dfs(i, j, k):
            # print(len(board), len(board[0]), board[i][j], word[k])
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            # tmp, board[i][j] = board[i][j], '/'
            tmp = board[i][j]
            board[i][j] = '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            # print(res)
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                # print(1)
                if dfs(i, j, 0):
                    return True
        return False

        #
        # def check_positon(self, current_list_position, current_element_position,current_val, next_element):
        #     # down
        #     if 0 <= current_list_position < len(board) and 0 <= current_element_position < len(board[0])-1:
        #         # print(current_list_position,current_element_position,current_val)
        #         # print(current_list_position, current_element_position, next_element)
        #         if self.board[current_list_position + 1][current_element_position] == next_element:
        #             print(1)
        #             return current_list_position + 1, current_element_position, True
        #         # right
        #         elif self.board[current_list_position][current_element_position + 1] == next_element:
        #             print(2)
        #             return current_list_position, current_element_position + 1, True
        #         # left
        #         elif self.board[current_list_position][current_element_position - 1] == next_element:
        #             print(3)
        #             return current_list_position, current_element_position - 1, True
        #         # up
        #         elif self.board[current_list_position - 1][current_element_position] == next_element:
        #             print(4)
        #             return current_list_position - 1, current_element_position, True
        #     else:
        #         return False
        #
        #
        #
        # # current_list_position=0
        # # current_element_position=0
        # for idx, val in enumerate(self.word_list):
        #     for key, matrix in enumerate(board):
        #         if val in matrix:
        #
        #             # print(val, matrix)
        #             a, b,is_valid = check_positon(self, key, idx,val, self.word_list[idx+1])
        #             # print(a, b,is_valid)
        #             if is_valid:
        #                 break
        #             else:
        #                 continue

        # 循环 word_list
        # current_list_position=0
        # current_element_position=0
        # for idx, val in enumerate(word_list):
        #     i = 0
        #     while i in range(i, len(board)):
        #         if val in board[i]:
        #             current_list_position, current_element_position = Solution.check_positon(self, current_list_position,
        #                                                                                      current_element_position,
        #                                                                                   word_list[idx + 1])
        #         i += 1









        #     if val in board[idx] and is_valid_position:
        #         print(val)
        #         current_list_position = key
        #         current_element_position = matrix.index(val)
        #         next_element = word_list[idx+1]
        #         is_valid_position = Solution.check_positon(self, current_list_position, current_element_position,next_element)
        #         # print(val, is_valid_position)










    #             if val in matrix and idx == 0:
    #                 point = matrix.index(val)
    #                 coordinate = Solution.get_coordinate(self, point, key)
    #                 # print(coordinate)
    #                 break
    #
    #             elif val in matrix and (coordinate.get('right') == str(key) + str(point + 1)
    #                                     or coordinate.get('down') == str(key + 1) + str(point)):
    #                 point = matrix.index(val)
    #                 coordinate = Solution.get_coordinate(self, point, key)
    #                 break
    #             # return '1'
    #
    # def get_coordinate(self, point, key):
    #     coordinate_point = {}
    #     if point == 0 and key == 0:
    #         coordinate_point['up'] = ''
    #         coordinate_point['down'] = str(key + 1) + str(point)
    #         coordinate_point['left'] = ''
    #         coordinate_point['right'] = str(key) + str(point + 1)
    #     print(point, key, coordinate_point)
    #     return coordinate_point








# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]
# word = "ABCCED"
# board = [["a","b"],["c","d"]]
# word = "abcd"
board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"


a = Solution(board, word)
a.exist()