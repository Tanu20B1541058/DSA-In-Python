from collections import deque
class Solution:
    def minReorder(self, n: int, connections) -> int:
        graph = []
        for i in range(n):
            graph.append(list())
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(-edge[0])
        visited = [False]*n
        count = 0
        q = deque()
        q.append(0)
        visited[0] = True
        while q:
            curr = q.popleft()
            for nbr in graph[abs(curr)]:
                if not visited[abs(nbr)]:
                    q.append(nbr)
                    visited[abs(nbr)] = True
                    if nbr > 0:
                        count += 1
        return count
        
        