import math
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:

        def buildGraph(edges, nodes):
            graph = []
            for i in range(nodes):
                graph.append(list())
            for edge in edges:
                graph[edge[0]].append((edge[1], edge[2]))
            return graph
        def shortestPath(edges, nodes, src, k):
            graph = buildGraph(edges, nodes)
            queue = deque()
            distance = [math.inf] * (nodes)
            distance[src] = 0
            stops = 0
            queue.append((distance[src], src, stops))

            while queue:
                curr_distance, curr_node, curr_stops = queue.popleft()
                
                if curr_stops > k:
                    continue
                for nbr_pair in graph[curr_node]:
                    new_distance = curr_distance + nbr_pair[1]
                    
                    if new_distance < distance[nbr_pair[0]] and curr_stops <= k:
                        distance[nbr_pair[0]] = new_distance
                        queue.append((distance[nbr_pair[0]], nbr_pair[0], curr_stops+1))
                    
            return distance
        
        ans = shortestPath(flights, n, src, k)
        if ans[dst] == math.inf:
            return -1
        return ans[dst]       