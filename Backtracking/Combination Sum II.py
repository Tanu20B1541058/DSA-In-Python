def combinationSum2(candidates, target):
        subset=[]
        powerset=[]
        candidates.sort()
        

        def solve(nums,target,subset,powerset,i,s):
            if s ==target:
                powerset.append(subset.copy())
                return
            if i ==len(nums):
                return
            if s>target:
                return
            subset.append(nums[i])
            solve(nums,target,subset,powerset,i+1,s+nums[i])
            subset.pop()
            while (i<len(nums)-1 and nums[i]==nums[i+1]):
                i +=1

            solve(nums,target,subset,powerset,i+1,s)
        solve(candidates,target,subset,powerset,0,0)
        return powerset
candidates = [10,1,2,7,6,1,5] 
target = 8
print(combinationSum2(candidates, target))