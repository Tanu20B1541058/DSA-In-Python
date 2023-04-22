import math
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        
        dp = [[0]*N for _ in range(N)]
        for i in range(N-1, 0, -1):
            for j in range(i+1, N):
                min_cost = math.inf
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                    min_cost = min(min_cost, cost)
                dp[i][j] = min_cost
        return dp[1][N-1]
                