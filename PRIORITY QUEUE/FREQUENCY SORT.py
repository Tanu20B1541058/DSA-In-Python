from heapq import *
class FrequencySort:
    
    def frequencysort(s):
        map=dict()
        for char in s:
            map[char]=map.get(char,0)+1
        max_heap=[]
        for key,value in map.items():
            heappush(max_heap,(-value,key))
        ans=[]
        while max_heap:
            value,key=heappop(max_heap)
            freq=-value
            for i in range(freq):
                ans.append(key)
        return ''.join(ans)
                
if __name__=='__main__':
    s="ppppaaqrs"
    ans=FrequencySort.frequencysort(s)
    print(ans)
        
    