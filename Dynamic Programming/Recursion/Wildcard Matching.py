class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def unique(p,n):
            for i in range(n):
                if p[i] !='*':
                    return False
            return True
        def solve(s,p,m,n):
            if m==0 and n==0:
                return True
            if n==0:
                return False
            if m==0 and unique(p,n):
                return True
            elif m==0:
                return False
            elif s[m-1] ==p[n-1] or p[n-1]=='?':
                return solve(s,p,m-1,n-1)
            elif p[n-1]=='*':
                flag=False
                for i in range(m+1):
                    flag = flag or solve(s,p,m-i,n-1)
                    if flag:
                        return True
                return flag
            else:
                return False
        ans =solve(s,p,len(s),len(p))
        return ans