class Solution:
    def makeConnected(self, n: int, connections) -> int:
        if len(connections) < n -1:
            return -1 
       
        def union(u, v, parent):
            pu = find(u, parent)
            pv = find(v, parent)
            if pu != pv:
                parent[pv] = pu
        
        def find(u, parent):
            if u == parent[u]:
                return u
            return find(parent[u], parent)
        cable = len(connections)
        count = 0
        parent = []*n
        for i in range(n):
            parent.append(i)
        for edge in connections:
            u = min(find(edge[0], parent), find(edge[1], parent))
            v = max(find(edge[0], parent), find(edge[1], parent))
            if find(u, parent) == find(v, parent):
                count += 1
            else:
                union(u, v, parent)
        print(count)
        print(parent)
        seen = set()
        for i in parent:
            x = find(i, parent)
            seen.add(x)
        return len(seen)-1
        
