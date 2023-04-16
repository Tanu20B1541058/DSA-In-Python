class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def solve(n, dp):
            if dp[n] != -1:
                return dp[n]
            if n==0:
                dp[n] = 1
                return dp[n]
            elif n<0:
                dp[n] = 0
                return dp[n]
            else:
                left=solve(n-1, dp)
                right=solve(n-2, dp)
            dp[n] = left+right
            return dp[n]
        ans=solve(n, dp)
        return ans
    