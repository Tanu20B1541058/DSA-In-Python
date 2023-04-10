import math 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c=0
        if len(t)>len(s):
            return ""
        ansStart ,ansEnd=0,0
        map=dict()
        for ch in t:
            map[ch]=map.get(ch,0)+1
        matched=0
        ws=0
        ans=""
        length=math.inf
        for we in range(len(s)):
            currChar=s[we]
            if currChar in map:
                map[currChar] -=1
                if map[currChar]==0:
                    matched +=1
            while matched==len(map):
                #length=min(length,we-ws+1)
                if (we-ws+1 <length):
                    length=we-ws+1
                    ansStart=ws
                    ansEnd=we
                leftChar=s[ws]
                ws +=1
                if leftChar in map:
                    if map[leftChar]==0:
                        matched -=1
                    map[leftChar] +=1
                c +=1
        
        if (ansStart ==ansEnd and s[ansStart] not in map ) or c==0:
            return ""
        else:

            while(ansStart<=ansEnd):
                ans +=s[ansStart]
                ansStart +=1
            return ans
                
