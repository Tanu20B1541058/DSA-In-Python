res=[]
def solve(s, l, r):
    if l == r:
        res.append(''.join(s))
    else:
        for i in range(l, r+ 1):
            s[l], s[i] = s[i], s[l]
            solve(s, l + 1, r)
            s[l], s[i] = s[i], s[l]
 
 
def allPermute():
    str = "ABC"
    N = len(str)
    s = list(str)
    
    solve(s, 0, N - 1)
    
allPermute()
print(res)