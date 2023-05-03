
import math
class Solution:
    def maxCoins(self, nums) -> int:
        def solve(i, j, arr):
            if i> j :
                return 0
            max_cost = -math.inf
            for k in range(i, j+1):
                cost = arr[i-1]*arr[k]*arr[j+1] + solve(k+1,j, arr) + solve(i, k-1, arr)
                max_cost = max(max_cost, cost)
            return max_cost
        
        n = len(nums)
        arr = [1]*(n+2)
        for i in range(0,n):
            arr[i+1] = nums[i]
        
        return solve(1, n, arr)