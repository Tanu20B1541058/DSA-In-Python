class Solution:
    def findRedundantConnection(self, edges) :
        parent = [0]*(len(edges)+1)
        for i in range(1,len(edges)):
            parent[i]=i
        
        def union(u, v, parent):
            pu = find(u, parent)
            pv = find(v, parent)
            
            parent[pv] = pu
            
        def find(node, parent):
            if parent[node] == node:
                return node
            return find(parent[node] , parent)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if find(u, parent) == find(v, parent):
                return edge
            else:
                union(u, v, parent)
        
        