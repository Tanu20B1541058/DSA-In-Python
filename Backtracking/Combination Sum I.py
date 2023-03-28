def combinationSum(candidates, target):
        subset=[]
        powerset=[]
        candidates.sort()
        

        def solve(nums,subset,powerset,i,target,s):
            if s==target:
                powerset.append(subset.copy())
                return
            if i ==len(nums):
                return
            if s>target:
                return
            #include
            

            subset.append(nums[i])
            
            solve(nums,subset,powerset,i,target,s+nums[i])
            subset.pop()

            #ignore
            solve(nums,subset,powerset,i+1,target,s)
        solve(candidates,subset,powerset,0,target,0)
        return powerset
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))