from heapq import *
class Solution:
    def findRelativeRanks( score):
        medal=["Gold Medal","Silver Medal","Bronze Medal"]
        ans=[0]*len(score)
        max_heap=[]
        for i in range(len(score)):
            heappush(max_heap,(-score[i],i))
        
        r=1
        while max_heap:
            s,i=heappop(max_heap)
            if r<=3:
                ans[i]=medal[r-1]
            else:
                ans[i]=str(r)
            r +=1
        return ans
if __name__=='__main__':
    score = [5,4,3,2,1]
    print(Solution.findRelativeRanks( score))