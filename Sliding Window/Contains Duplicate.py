def ContainsDuplicate(arr,k):
    map={}
    for we in range(len(arr)):
        currChar=arr[we]
        if currChar in map:
            ws=map[currChar]
            if (we-ws <=k):
                return True
        map[currChar]=we
    return False
arr=[1, 0, 1, 1]
k=1
print(ContainsDuplicate(arr,k))