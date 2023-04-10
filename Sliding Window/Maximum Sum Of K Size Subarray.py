import math
def MaximumSumSub(arr,k):
    ans=-math.inf
    ws=0
    wsum=0
    for we in range(len(arr)):
        wsum +=arr[we]
        if we<=k-1:
            ans=max(ans,wsum)
            wsum=wsum-arr[ws]
            ws=ws+1
    return ans
arr=[2, 6, -9, 7, -1, 5, 4]
k=3
print(MaximumSumSub(arr,k))
    