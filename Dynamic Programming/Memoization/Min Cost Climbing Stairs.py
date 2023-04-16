class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        def solve(cost,n, dp):
            if n<=1:
                return 0
            if dp[n] != -1:
                return dp[n]
            left=cost[n-1]+solve(cost,n-1, dp)
            right=cost[n-2]+solve(cost,n-2, dp)
            dp[n] = min(left,right)
            return dp[n]
        dp = [-1]*(len(cost)+1)
        return solve(cost,len(cost), dp)