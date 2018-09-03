#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  :  2018/4/21 下午8:26


"""

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        map_count = dict()
        for i in range(len(grid)):
            column_length = len(grid[i])
            for j in range(column_length):
                if int(grid[i][j]) == 1:
                    if i - 1 >= 0 and int(grid[i - 1][j]) == 1:
                        map_count[(i, j)] = (i - 1, j)
                    if j - 1 >= 0 and int(grid[i][j - 1]) == 1:
                        if (i, j) in map_count:
                            map_count[(i, j)] = [(map_count[(i, j)]), (i, j - 1)]
                        else:
                            map_count[(i, j)] = (i, j - 1)
                    if (i, j) not in map_count:
                        map_count[(i, j)] = None
        for key, value in map_count.iteritems():
            if value is None:
                count += 1
            elif isinstance(value, list):
                count -= 1
        return count


class Solution1(object):
    def numIsLands(self, grid):
        ans = 0
        if not len(grid):
            return ans
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for x in range(m)]  # m * n
        self.grid = grid
        self.visited = visited
        self.m = m
        self.n = n
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1' and not visited[x][y]:
                    ans += 1
                    self.bfs(grid, visited, x, y, m, n)
        return ans

    # 广度优先搜索
    def bfs(self, grid, visited, x, y, m, n):
        dz = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(x, y)]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in dz:
                np = (front[0] + p[0], front[1] + p[1])
                if self.isValid(np, m, n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
                    visited[np[0]][np[1]] = True
                    queue.append(np)

    def dfs(self, x, y):
        dz = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for p in dz:
            np = (x + p[0], y + p[1])
            if self.isValid(np, self.m, self.n) and self.grid[np[0]][np[1]] == '1' and not self.visited[np[0]][np[1]]:
                self.visited[np[0]][np[1]] = True
                self.dfs(np[0], np[1])

    def isValid(self, np, m, n):
        return m > np[0] >= 0 and n > np[1] >= 0



if __name__ == '__main__':
    solution = Solution1()
    print solution.numIsLands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]])
