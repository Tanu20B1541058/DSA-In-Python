###No repeat substring
def NoRepeatsubstring(st):
    map=dict()
    ws=0
    mxlength=0
    for we in range(len(st)):
        currChar=st[we]
        if (currChar in map):
            if ws<=map[currChar]:
                ws=map[currChar]+1
        
        map[currChar]=we
        if mxlength<(we-ws+1):
            mxlength=we-ws+1
    print(mxlength)
    
                

st="baabcd"
NoRepeatsubstring(st)       