#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/1/9 下午5:18


class Solution(object):
    def sudo(self, board):
        for i in range(9):
            if not self.is_valid_sudo(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.is_valid_sudo(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[s][t] for s in [i, i + 1, i + 2] for t in [j, j + 1, j + 2]]
                if not self.is_valid_sudo(block):
                    return False
        return True

    def is_valid_sudo(self, data):
        map = {}
        for c in data:
            if c != '.':
                if c in map:
                    return False
                else:
                    map[c] = True
        return True


class Solution2(object):
    def sudo(self, board):
        row = [[False] * 9 for i in range(9)]
        col = [[False] * 9 for i in range(9)]
        block = [[False] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i / 3 * 3 + j / 3
                    if row[i][num] or col[j][num] or block[k][num]:
                        return False
                    row[i][num] = col[j][num] = block[k][num] = True
        return True


if __name__ == '__main__':
    solution = Solution()
    board = [[".","8","7","6","5","4","3","2","1"],
             ["2",".",".",".",".",".",".",".","."],
             ["3",".",".",".",".",".",".",".","."],
             ["4",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".",".","."],
             ["6",".",".",".",".",".",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             ["8",".",".",".",".",".",".",".","."],
             ["9",".",".",".",".",".",".",".","."]]
    print solution.sudo(board)