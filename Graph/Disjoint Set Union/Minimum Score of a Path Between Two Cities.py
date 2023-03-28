import math
class Solution:
    def minScore(self, n: int, roads) -> int:
        def union(u,v,parent):
            parent[v]=u


        def find(node,parent):
            if parent[node]==node:
                return node
            return find(parent[node],parent)

        
        parent=[]*(n+1)
        for i in range(n+1):
            parent.append(i) 
        for edge in roads:
            u = min(find(edge[0], parent), find(edge[1], parent))
            v = max(find(edge[0], parent), find(edge[1], parent))
            if u != v:
                union(u,v,parent)
        ans = math.inf
        print(parent)
        for edge in roads:
            v = max(find(edge[0], parent), find(edge[1], parent))
            if parent[v] == 1:
                ans = min(ans, edge[2])
        return ans
        
            
