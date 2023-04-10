from heapq import *
class Solution:
    def maxPerformance( n, speed, efficiency, k):
        team=[]
        for i in range(n):
            team.append([speed[i],efficiency[i]])
        
        team.sort(key= lambda x:x[1] ,reverse=True)
        
        min_heap=[]
        max_performance=0
        totalspeed=0
        
        for i in range(len(team)):
            
            while len(min_heap)>=k:
                c=heappop(min_heap)
                totalspeed -=c

            totalspeed += team[i][0]
            heappush(min_heap,team[i][0])
            max_performance=max(max_performance,totalspeed*team[i][1])

        return max_performance %(10**9 +7)
if __name__=='__main__':
    n = 6 
    speed = [2,10,3,1,5,8] 
    efficiency = [5,4,3,9,7,2]
    k = 2
    print(Solution.maxPerformance( n, speed, efficiency, k))