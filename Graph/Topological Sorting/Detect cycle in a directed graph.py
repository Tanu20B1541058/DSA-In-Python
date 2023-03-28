from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        def build_indegree(v, edges):
            indegree = [0 for i in range(v)]
            for node in range(v):
                for edge in edges[node]:
                    indegree[edge] += 1
            return indegree
        def topological_sorting(v, edges):
            indegree = build_indegree(v, edges)
            queue = deque()
            for i in range(v):
                if indegree[i] == 0:
                    queue.append(i)
            sorted_order = []
            while queue:
                curr_node = queue.popleft()
                sorted_order.append(curr_node)
                for nbr in edges[curr_node]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)
            if len(sorted_order) == v:
                return False
            else:
                return True
        return topological_sorting(V, adj)