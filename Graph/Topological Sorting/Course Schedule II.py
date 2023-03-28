from collections import deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        def build_graph(v, edges):
            graph = []
            indegree = dict()
            for i in range(v):
                graph.append(list())
                indegree[i] = 0
            for edge in edges:
                graph[edge[0]].append(edge[1])
                indegree[edge[1]] += 1
            return graph,indegree
        def topological_sorting(v, edges):
            graph, indegree = build_graph(v, edges)
            queue = deque()
            for key, value in indegree.items():
                if value == 0:
                    queue.append(key)
            sorted_order = []
            while queue:
                curr_node = queue.popleft()
                sorted_order.append(curr_node)
                for nbr in graph[curr_node]:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)
            if len(sorted_order) == v:
                return sorted_order[::-1]
            else:
                return []
        return topological_sorting(numCourses, prerequisites)