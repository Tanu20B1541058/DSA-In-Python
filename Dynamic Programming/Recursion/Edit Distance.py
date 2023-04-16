class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(w1,w2,m,n):
            if m==0:
                return n
            if n==0:
                return m
            if w1[m-1]==w2[n-1]:
                return solve(w1,w2,m-1,n-1)
            return 1+min(solve(w1,w2,m-1,n),solve(w1,w2,m,n-1),solve(w1,w2,m-1,n-1))
        return solve(word1,word2,len(word1),len(word2))
       