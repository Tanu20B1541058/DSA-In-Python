class Solution:
    def lengthOfLIS(self, nums) -> int:
        def solve(arr, n, curr, prev):
            if curr == n:
                return 0
            #considerable
            include = 0
            if prev == -1 or arr[curr] > arr[prev]:
                include =  1 + solve(arr, n, curr+1, curr)
            
            # exclude 
            exclude = solve(arr, n, curr+1, prev)

            return max(include, exclude)
        return solve(nums, len(nums), 0, -1)
