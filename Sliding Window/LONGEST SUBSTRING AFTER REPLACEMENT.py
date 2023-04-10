import math
def longestSubstring(s,k):
    ws=0
    maxlength=0
    maximumFrequency=0
    Hmap=dict()
    for we in range(len(s)):
        currChar=s[we]
        Hmap[currChar]=Hmap.get(currChar,0)+1
        maximumFrequency=max(maximumFrequency,Hmap[currChar])
        if ((we-ws+1)-maximumFrequency>k):
            leftChar=s[ws]
            Hmap[leftChar]=Hmap.get(leftChar,0)-1
            ws=ws+1
        maxlength=max(maxlength,we-ws+1)
    return maxlength

    
s="abab"
k=2
print(longestSubstring(s,k))
