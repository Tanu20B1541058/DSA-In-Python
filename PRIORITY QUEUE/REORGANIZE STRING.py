from heapq import *
class ReorganizeString:
    def reorganizestring(s):
        map=dict()
        for char in s:
            map[char]=map.get(char,0)+1
        max_heap=[]
        for key,value in map.items():
            heappush(max_heap,(-value,key))
        ans=[]
        while (len(max_heap)>=2):
            value1,key1=heappop(max_heap)
            f1=-value1
            value2,key2=heappop(max_heap)
            f2=-value2
            
            ans.append(key1)
            ans.append(key2)
            
            f1 -=1
            f2 -=1
            if(f1>0):
                heappush(max_heap,(-f1,key1))
            if(f2>0):
                heappush(max_heap,(-f2,key2))
        if len(max_heap)==0:
            return ''.join(ans)
        else:
            value,key=heappop(max_heap)
            f=-value
            if f==1:
                ans.append(key)
                return ''.join(ans)
            else:
                return ''
            
            
            
if __name__=='__main__':
    s="aaaaaabcddd"
    ans=ReorganizeString.reorganizestring(s)
    print(ans)       
    