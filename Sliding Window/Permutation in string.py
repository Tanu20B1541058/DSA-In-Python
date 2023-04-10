def PermutationString(s,p):
    map=dict()
    for ch in p:
        map[ch]=map.get(ch,0)+1
    ws=0
    matched=0
    for we in range(len(s)):
        currChar=s[we]
        if currChar in map:
            map[currChar] -=1
            if map[currChar]==0:
                matched +=1
        if matched==len(map):
            return True
        if we>=len(p)-1:
            leftChar=s[ws]
            ws +=1
            if leftChar in map:
                if map[leftChar]==0:
                    matched -=1
                map[leftChar] +=1
    return False
s="ccchellocc"
p="ocl"
print(PermutationString(s,p))