import math
class Solution:
    def minCost(self, stickLength: int, cuts) -> int:
        n=len(cuts)
        arr = [0]*(n+2)
        for i in range(n):
            arr[i+1] = cuts[i]
        arr[n+1] = stickLength
        arr.sort()
        dp=[[0 for _ in range(n+2)]for _ in range(n+2)]
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                min_cost = math.inf
                for k in range(i,j+1):
                    cost = dp[i][k-1] + dp[k+1][j] + arr[j+1] - arr[i-1]
                    min_cost = min(min_cost, cost)
                dp[i][j]=min_cost
        return dp[1][n]
        
        
        
        
        
