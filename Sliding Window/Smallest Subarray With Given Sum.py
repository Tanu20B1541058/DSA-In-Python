import math
def SmallestSubSum(arr,s):
    wl=math.inf
    ws=0
    wsum=0
    for we in range(len(arr)):
        wsum +=arr[we]
        while (wsum>=s):
            wl=min(wl,we-ws+1)
            wsum=wsum-arr[ws]
            ws +=1
    if wl==math.inf:
        return 0
    else:
        return wl
arr=[2, 1, 4, 5, 1, 3]
s=7
print(SmallestSubSum(arr,s))