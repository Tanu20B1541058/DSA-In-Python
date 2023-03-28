from heapq import *
import math
class Solution:
    def minScore(self, n: int, roads) -> int:
        def build_graph(nodes, edges):
            graph = []
            for i in range( nodes+1):
                graph.append(list())
            for edge in edges:
                graph[edge[0]].append((edge[1], edge[2]))
                graph[edge[1]].append((edge[0], edge[2]))
            return graph
        graph = build_graph(n, roads)
        print(graph)
        distance = [math.inf]*(n+1)
        
        min_heap = []
        heappush(min_heap, (distance[1], 1))

        while min_heap:
            curr_distance, curr_node = heappop(min_heap)
            for nbr_pair in graph[curr_node]:
                new_distance = min(curr_distance, nbr_pair[1])
                if new_distance < distance[nbr_pair[0]]:
                    distance[nbr_pair[0]] = new_distance
                    heappush(min_heap, (new_distance, nbr_pair[0]))
        return distance[n]
        
        