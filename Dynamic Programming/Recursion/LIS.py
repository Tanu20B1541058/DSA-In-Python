#### Binary search
class Solution:
    def lengthOfLIS(self, nums) -> int:
        def lower_bound(arr,target):
            left=0
            right=len(arr)
            while left<right:
                mid=(left+right)//2
                if arr[mid]<target:
                    left=mid + 1
                else:
                    right=mid
            return left
        SortedArray=[]
        SortedArray.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>SortedArray[-1]:
                SortedArray.append(nums[i])
            else:
                lowerNumber=lower_bound(SortedArray,nums[i])
                SortedArray[lowerNumber]=nums[i]
        return len(SortedArray)


#############  space optimized
class Solution:
    def lengthOfLIS(self, nums) -> int:
       dp = [1]*(len(nums))
       mxlength = 1
       for i in range(1,len(nums)):
           for j in range(i-1, -1 ,-1):
               if nums[i] > nums[j]:
                   dp[i] = max(dp[i], 1+dp[j])
                   mxlength = max(mxlength, dp[i])
       return mxlength
        