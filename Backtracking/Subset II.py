def subsetsWithDup(nums):
    subset=[]
    powerset=[]
    nums.sort()


    def solve(nums,subset,powerset,i):
        if i==len(nums):
            powerset.append(subset.copy())
            return
        #include
        subset.append(nums[i])
        solve(nums,subset,powerset,i+1)
        subset.remove(nums[i])

        #ignore
        while (i<len(nums)-1 and nums[i]==nums[i+1]):
            i +=1
        solve(nums,subset,powerset,i+1)
    solve(nums,subset,powerset,0)
    return powerset
nums=[1,2,2]
print(subsetsWithDup(nums))