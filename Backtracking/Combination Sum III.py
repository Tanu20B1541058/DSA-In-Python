class Solution:
    def combinationSum3(self, k: int, n: int) :
        powerset, subset = [], []
        nums = [1,2,3,4,5,6,7,8,9]
        def solve(subset, powerset, i, sm, target): 
            
            if i>=len(nums):
                if sm == target and len(subset) == k:
                    powerset.append(subset.copy())
                return
            if sm>target or len(subset)>k:
                return 
            if sm == target and len(subset) == k:
                powerset.append(subset.copy())
                return
            
             #include
            subset.append(nums[i])
            solve(subset, powerset, i+1, sm+nums[i], target)
            subset.pop()
                
            solve(subset, powerset, i+1, sm, target) #exclude
        solve(subset, powerset, 0, 0, n)
        return powerset