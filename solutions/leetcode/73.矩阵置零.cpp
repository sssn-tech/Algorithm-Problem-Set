/*
 * @lc app=leetcode.cn id=73 lang=cpp
 *
 * [73] 矩阵置零
 */

// @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        row_first = (0 in matrix[0])
        col_fisrt = (0 in [row for row in list(zip(*matrix))][0])
        # print(row_first, col_fisrt)
        # print([list(row) for row in list(zip(*matrix))])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # print(matrix)
        for i in range(1, n):
            if matrix[i][0] == 0:
                matrix[i] = [0 for _ in range(m)]

        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0
        if row_first:
            matrix[0] = [0 for _ in range(m)]
        if col_fisrt:
            for i in range(n):
                matrix[i][0] = 0

// @lc code=end

