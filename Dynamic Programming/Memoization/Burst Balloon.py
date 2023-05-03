import math
class Solution:
    def maxCoins(self, nums) -> int:
        def solve(i, j, arr, dp):
            if i> j :
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            max_cost = -math.inf
            for k in range(i, j+1):
                cost = arr[i-1]*arr[k]*arr[j+1] + solve(k+1,j, arr, dp) + solve(i, k-1, arr, dp)
                max_cost = max(max_cost, cost)
            dp[i][j] = max_cost
            return dp[i][j]
        
        n = len(nums)
        arr = [1]*(n+2)
        for i in range(0,n):
            arr[i+1] = nums[i]
        dp = [[-1]*(n+1) for _ in range(n+1)]
        
        return solve(1, n, arr, dp)