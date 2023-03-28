from collections import deque

class Solution:
    def longestCycle(self, edges) -> int:
        set_ = self.findOrder(len(edges), edges)
        if len(set_) == len(edges):
            return -1

        comp = self.Isconnected(edges)
        max_ = 0
        for i in range(len(comp)):
            c = 0
            for j in range(len(comp[i])):
                if comp[i][j] not in set_:
                    c += 1
            max_ = max(c, max_)
        return max_

    def findOrder(self, n: int, pre):
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for i in range(n):
            if pre[i] == -1:
                continue
            indegree[pre[i]] += 1
            adj[i].append(pre[i])
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        i = 0
        topo = [0] * n
        set_ = set()
        while q:
            node = q.popleft()
            set_.add(node)
            topo[i] = node
            i += 1

            for e in adj[node]:
                indegree[e] -= 1
                if indegree[e] == 0:
                    q.append(e)
        return set_

    def Isconnected(self, edges):
        adj = [[] for _ in range(len(edges))]
        comp = []
        for i in range(len(edges)):
            if edges[i] == -1:
                continue
            adj[i].append(edges[i])
            adj[edges[i]].append(i)
        vis = [False] * len(edges)
        for i in range(len(edges)):
            if not vis[i]:
                temp = []
                q = deque()
                q.append(i)
                while q:
                    node = q.popleft()
                    if vis[node]:
                        continue
                    temp.append(node)
                    vis[node] = True
                    for e in adj[node]:
                        if not vis[e]:
                            q.append(e)
                comp.append(temp)
        return comp