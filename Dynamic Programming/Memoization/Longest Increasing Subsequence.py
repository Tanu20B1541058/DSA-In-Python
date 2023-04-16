class Solution:
    def lengthOfLIS(self, nums) -> int:
        def solve(arr, n, curr, prev, dp):
            if curr == n:
                return 0
            if dp[curr][prev+1] != -1:
                return dp[curr][prev+1]
            #considerable
            include = 0
            if prev == -1 or arr[curr] > arr[prev]:
                include =  1 + solve(arr, n, curr+1, curr, dp)
            
            # exclude 
            exclude = solve(arr, n, curr+1, prev, dp)

            dp[curr][prev+1] = max(include, exclude)
            return dp[curr][prev+1]

        dp = [[-1]*(len(nums)+1) for _ in range(len(nums))]
        return solve(nums, len(nums), 0, -1, dp)
