from heapq import *
from collections import deque
class ReorganizeStringKDiastanceAPart:
    
    @staticmethod
    def reorganizeString(s,k):
        map=dict()
        for ch in s:
            map[ch]=map.get(ch,0)+1
        
        max_heap=[]
        for key,value in map.items():
            heappush(max_heap,(-value,key))
        
        queue=deque()
        ans=[]
        
        while max_heap:
            val,key=heappop(max_heap)
            f=-val
            
            ans.append(key)
            f -=1
            queue.append((key,f))
            
            if len(queue)==k:
                ch,val=queue.popleft()
                if val>0:
                    heappush(max_heap,(-val,ch))
        
        if len(ans)==len(s):
            return ''.join(ans)
        else:
            return ""
            
            
        
        
    
if __name__=='__main__':
    s="aabbcc"
    k=3
    ans=ReorganizeStringKDiastanceAPart.reorganizeString(s,k)
    print(ans)
    