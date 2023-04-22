import math 
class Solution:
    def minScoreTriangulation(self, values) -> int:
        N = len(values)
        dp = [[0]*N for _ in range(N)]
        for i in range(N-1, 0, -1):
            for j in range(i+1, N):
                min_cost = math.inf
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + values[i-1]*values[k]*values[j]
                    min_cost = min(min_cost, cost)
                dp[i][j] = min_cost
        return dp[1][N-1]