class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        def solve(cost,n):
            if n<=1:
                return 0
            left=cost[n-1]+solve(cost,n-1)
            right=cost[n-2]+solve(cost,n-2)
            return min(left,right)
        return solve(cost,len(cost))