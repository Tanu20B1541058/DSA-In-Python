from heapq import *
class LargestKElements:
    @staticmethod
    def largestkelements(arr,k):
        min_heap=[]
        for i in range(len(arr)):
            heappush(min_heap,arr[i]*-1)
            if(len(min_heap)==k+1):
                heappop(min_heap)
        ans=[]
        while min_heap:
            ans.append(heappop(min_heap)*-1)
        return ans
if __name__=='__main__':
    arr=[1,4,5,3,7,8,6,10]
    k=3
    ans=LargestKElements.largestkelements(arr,k)
    for a in ans:
        print(a,end=" ")
