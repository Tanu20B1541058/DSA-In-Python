class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def check(p,n):
            for i in range(n-1, -1, -2):
                if p[i] != '*':
                    return False
            return True 
        def solve(s, p, m, n, dp):
            if m == 0 and n == 0:
                return 1
            if n == 0:
                return 0
            if m == 0 and check(p, n):
                return 1
            if m == 0:
                return 0
            if dp[m][n] != -1:
                return dp[m][n]
            if s[m-1] == p[n-1] or p[n-1] == '.':
                dp[m][n] = solve(s, p, m-1, n-1, dp)
                return dp[m][n]
            if p[n-1] == '*':
                if p[n-2] == ".":
                    flag = 0
                    for i in range(m+1):
                        flag = flag or solve(s,p, m-i, n-2, dp)
                        if flag == 1:
                            dp[m][n] = 1
                            return dp[m][n]
                    dp[m][n] = flag
                    return dp[m][n]
                else:
                    flag = 0
                    for i in range(m+1):
                        if i == 0:
                            flag = flag or solve(s, p, m-i, n-2, dp)
                            if flag == 1:
                                dp[m][n] = 1
                                return dp[m][n]
                        else:
                            if s[m-i] == p[n-2]:
                                flag = flag or solve(s, p, m-i, n-2, dp)
                                if flag == 1 :
                                    dp[m][n] = 1
                                    return dp[m][n]
                            else:
                                dp[m][n] = 0
                                return dp[m][n]
            else:
                dp[m][n] = 0
                return dp[m][n] 
        dp = [[-1]*(len(p)+1) for _ in range(len(s)+1)]
        ans = solve(s, p, len(s), len(p), dp)
        if ans == 1:
            return True
        return False


                        
                    

            

        