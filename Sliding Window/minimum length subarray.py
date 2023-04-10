#minimum length subarray whose sum >=targetsum
def minSubArray(arr,targetsum):
    ws=0
    wsum=0
    minilength=1000000
    for we in range(len(arr)):
        wsum=wsum+arr[we]
        while (wsum>=targetsum):
            if minilength>(we-ws+1):
                minilength=we-ws+1
            wsum=wsum-arr[ws]
            ws=ws+1
    print(minilength)
            
arr=[3,4,7,2,10,1]
targetsum=12
minSubArray(arr,targetsum)