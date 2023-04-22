import math
class Solution:
    def minCost(self, stickLength: int, cuts) -> int:
        def solve(i, j, arr, dp):
            if i> j :
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            min_cost = math.inf
            for k in range(i, j+1):
                cost = solve(i, k-1, arr, dp) + solve(k+1, j, arr, dp) + arr[j+1] - arr[i-1]
                min_cost = min(min_cost, cost)
            dp[i][j] = min_cost
            return dp[i][j]
        cuts.sort()
        n = len(cuts)
        arr = [0]*(n+2)
        for i in range(0,n):
            arr[i+1] = cuts[i]
        arr[n+1] = stickLength
        dp = [[-1]*(n+1) for _ in range(n+1)]
        return solve(1, n, arr, dp)