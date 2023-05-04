arr = [1, 2, 2, 3, 3, 4]
def checkSorted(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
    else:
        return True 
print(checkSorted(arr))



