#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/5/3 下午4:42


"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


"""


class Solution(object):
    def exist(self, board, word):
        """
        :param board:
        :param word:
        :return:
        """
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.word = word
        self.ans = list()
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    work_path = list()
                    self.ans.append(word[0])
                    work_path.append((i, j))
                    self.dfs(i, j, 1, work_path)
                    if ''.join(self.ans) == word:
                        return True
                    else:
                        self.ans = list()
                        continue
        return False

    def dfs(self, x, y, depth, walk_path):
        if depth >= len(self.word):
            return
        dz = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for p in dz:
            np = (x + p[0], y + p[1])
            if self.is_valid(np, self.m, self.n, walk_path) and self.board[np[0]][np[1]] == self.word[depth]:
                walk_path.append((np[0], np[1]))
                self.ans.append(self.board[np[0]][np[1]])
                if ''.join(self.ans) == self.word:
                    return
                self.dfs(np[0], np[1], depth + 1, walk_path)
        else:
            if ''.join(self.ans) == self.word:
                return
            else:
                self.ans.pop()
                walk_path.pop()

    def is_valid(self, np, m, n, walk_path):
        return m > np[0] >= 0 and n > np[1] >= 0 and np not in walk_path

if __name__ == '__main__':
    solution = Solution()
    print solution.exists([["b","a","b"],["b","b","a"],["b","b","b"]], "ab")
