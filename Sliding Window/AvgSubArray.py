def avgSubArray(arr,k):
    ans=[]
    ws=0
    wsum=0
    maxsum=0
    for we in range(len(arr)):
        wsum=wsum+arr[we]
        if (we>=k-1):
            ans.append(wsum/k)
            wsum =wsum-arr[ws]
            ws=ws+1
        
    print(ans)
    

            
arr=[1,2,3,4,5,6]
k=3
avgSubArray(arr,k)