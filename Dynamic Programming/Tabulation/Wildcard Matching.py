class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def unique(p,n):
            for i in range(n):
                if p[i] !='*':
                    return False
            return True
        

        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            for j in range(len(p)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif j == 0:
                    dp[i][j] = False
                elif i == 0 and unique(p,j):
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                elif s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False
        return dp[len(s)][len(p)]
        