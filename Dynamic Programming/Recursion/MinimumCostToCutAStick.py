import math 
class Solution:
    def minCost(self, stickLength: int, cuts) -> int:
        def solve(i, j, arr):
            if i> j :
                return 0
            min_cost = math.inf
            for k in range(i, j+1):
                cost = solve(i, k-1, arr) + solve(k+1, j, arr) + arr[j+1] - arr[i-1]
                min_cost = min(min_cost, cost)
            return min_cost
        cuts.sort()
        n = len(cuts)
        arr = [0]*(n+2)
        for i in range(0,n):
            arr[i+1] = cuts[i]
        arr[n+1] = stickLength
        return solve(1, n, arr)

