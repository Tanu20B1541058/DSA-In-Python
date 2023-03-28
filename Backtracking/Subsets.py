class Solution:
    def subsets(self, nums):
        subset=[]
        powerset=[]
        

        def solve(nums,subset,powerset,i):
            if i==len(nums):
                powerset.append(subset.copy())
                return
            #include
            subset.append(nums[i])
            solve(nums,subset,powerset,i+1)
            subset.remove(nums[i])

            #ignore
            solve(nums,subset,powerset,i+1)
        solve(nums,subset,powerset,0)
        return powerset