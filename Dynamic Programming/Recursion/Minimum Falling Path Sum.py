import math
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        def solve(row, col, matrix):
            if col < 0 or col >= len(matrix):
                return 10001
            if row == len(matrix)-1:
                return matrix[row][col]
            ans1 = matrix[row][col] + solve(row + 1, col - 1, matrix)
            ans2 = matrix[row][col] + solve(row + 1, col, matrix)
            ans3 = matrix[row][col] + solve(row + 1, col + 1, matrix)
            return min(ans1, ans2, ans3)

        n = len(matrix)
        min_path = math.inf
        for col in range(n):
            path = solve(0,col,matrix)
            min_path = min(min_path, path)
        return min_path