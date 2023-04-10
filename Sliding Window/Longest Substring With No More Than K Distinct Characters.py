import math
def LongestSubstringWithNoMoreThanKDistinctCharacters(st,k):
    sub=''
    ws=0
    length=-math.inf
    fmap={}
    for we in range(len(st)):
        rightChar=st[we]
        if rightChar in fmap:
            fmap[rightChar] +=1
        else:
            fmap[rightChar]=1
        while len(fmap)>k:
            leftChar=st[ws]
            fmap[leftChar] -=1
            if fmap[leftChar]==0:
                del fmap[leftChar]
            ws +=1
        #length=max(length,we-ws+1)
        if (we-ws+1 >length):
            length=we-ws+1
            ansStart=ws
            ansEnd=we
    while(ansStart<=ansEnd):
        sub +=st[ansStart]
        ansStart +=1
    print(sub)
    return length

        
st="araabdda"
k=3
print(LongestSubstringWithNoMoreThanKDistinctCharacters(st,k))