import math
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        def solve(i, j, arr):
            if i == j:
                return 0
            min_cost = math.inf
            for k in range(i, j):
                cost = solve(i, k, arr) + solve(k+1, j, arr) + arr[i-1]*arr[k]*arr[j]
                min_cost = min(min_cost, cost)
            return min_cost
        return solve(1, N-1, arr)
