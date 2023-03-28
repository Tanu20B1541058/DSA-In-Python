class KruskalAlgo:
    @staticmethod
    def find(u, parent):
        if u == parent[u]:
            return u
        return KruskalAlgo.find(parent[u], parent)
    
    def union(u, v, parent):
        p1 = KruskalAlgo.find(u, parent)
        p2 = KruskalAlgo.find(v, parent)
        parent[p2] = p1
        
    def mst(n, edges):
        parent = []*n
        for i in range(n):
            parent.append(i)
        edges.sort(key = lambda x : x[2])
        ans = 0
        for edge in edges:
            u, v, cost = edge[0], edge[1], edge[2]
            p1 = KruskalAlgo.find(u, parent)
            p2 = KruskalAlgo.find(v, parent)
            if p1 != p2:
                KruskalAlgo.union(p1, p2, parent)
                ans += cost
        return ans
    
    
if __name__ == '__main__':
    n = 6
    edges = [[0, 1, 8], [0, 2, 2], [1, 4, 1], [1, 5, 3],[2, 3, 6], [2,4,3], [3,5,4], [4,5,2]]
    print(KruskalAlgo.mst(n, edges))
    