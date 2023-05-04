class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(row, col):
            if row >= m or col >= n:
                return 0
            if row == m-1 and col == n-1:
                return 1
            return solve(row +1, col) + solve(row, col+1)
        return  solve(0,0)
       