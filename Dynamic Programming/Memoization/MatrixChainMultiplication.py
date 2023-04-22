import math
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        def solve(i, j, arr, dp):
            if i == j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            min_cost = math.inf
            for k in range(i, j):
                cost = solve(i, k, arr, dp) + solve(k+1, j, arr, dp) + arr[i-1]*arr[k]*arr[j]
                min_cost = min(min_cost, cost)
            dp[i][j] = min_cost
            return dp[i][j]
            
        dp = [[-1]*N for _ in range(N)]
        return solve(1, N-1, arr, dp)