class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [[0] * (n+1) for _ in range(n+1)]

        for ind in range(n-1, -1, -1):
            for prev in range(ind-1, -2, -1):
                len_ = 0 + dp[ind+1][prev+1]

                if prev == -1 or nums[ind] > nums[prev]:
                    len_ = max(len_, 1 + dp[ind+1][ind+1])

                dp[ind][prev+1] = len_

        return dp[0][-1+1]