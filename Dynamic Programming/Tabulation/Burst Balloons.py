import math
class Solution:
    def maxCoins(self, nums) -> int:
        
        n = len(nums)
        arr = [1]*(n+2)
        for i in range(0,n):
            arr[i+1] = nums[i]
        
        dp=[[0 for _ in range(n+2)]for _ in range(n+2)]
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                max_cost = -math.inf
                for k in range(i, j+1):
                    cost = arr[i-1]*arr[k]*arr[j+1] + dp[k+1][j] + dp[i][k-1]
                    max_cost = max(max_cost, cost)
                dp[i][j] = max_cost
        return dp[1][n]
        
        