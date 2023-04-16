class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def unique(p,n):
            for i in range(n):
                if p[i] !='*':
                    return False
            return True
        def solve(s,p,m,n,dp):
            if m==0 and n==0:
                return 1
            if n==0:
                return 0
            if dp[m][n] != -1:
                return dp[m][n]
            if m==0 and unique(p,n):
                return 1
            elif m==0:
                return 0
            elif s[m-1] ==p[n-1] or p[n-1]=='?':
                dp[m][n]= solve(s,p,m-1,n-1,dp)
                return dp[m][n]
            elif p[n-1]=='*':

                if solve(s, p, m-1, n, dp) == 1:
                    dp[m][n] = 1
                    return dp[m][n]
                if solve(s, p, m, n-1, dp) == 1:
                    dp[m][n] = 1
                    return dp[m][n]
                dp[m][n] = 0
                return dp[m][n]
            else:
                dp[m][n] = 0
                return dp[m][n]
                
        dp = [[-1]*(len(p)+1) for _ in range(len(s)+1)]
        ans =solve(s,p,len(s),len(p),dp)
        if ans == 0:
            return False
        return True