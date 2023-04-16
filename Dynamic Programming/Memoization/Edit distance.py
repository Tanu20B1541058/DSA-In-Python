class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def edit(w1, w2, m, n, dp):
            if m==0:
                return n
            if n==0:
                return m
            if dp[m][n] != -1:
                return dp[m][n]
            if w1[m-1]==w2[n-1]:
                dp[m][n] = edit(w1, w2, m-1, n-1, dp)
                return dp[m][n]
            dp[m][n] =  1+min(edit(w1, w2, m-1, n, dp), edit(w1, w2, m, n-1, dp), edit(w1, w2, m-1, n-1, dp))
            return dp[m][n]
        
        dp = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        return edit(word1, word2, len(word1), len(word2), dp)
       