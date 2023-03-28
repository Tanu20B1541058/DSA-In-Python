from collections import Counter
class Solution:
    def countPairs(self, n: int, edges) -> int:
        par=[i for i in range(n)]
        def find(a):
            if par[a]!=a:
                par[a]=find(par[a])
            return par[a]
        def union(a,b):
            temp1=find(a)
            temp2=find(b)
            par[temp1]=temp2
        for i,j in edges:
            union(i,j)
        l1=list(Counter([find(i) for i in range(n)]).values())
        temp=l1[0]
        ans=0
        for i in range(1,len(l1)):
            ans+=temp*l1[i]
            temp+=l1[i]
        return ans