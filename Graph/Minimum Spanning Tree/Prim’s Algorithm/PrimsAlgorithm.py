from heapq import *
import math
class Prims_Algorithm:
    
    def buildGraph(edges, nodes):
        graph = []
        for i in range(nodes + 1):
            graph.append(list())
        for edge in edges:
            graph[edge[0]].append((edge[1], edge[2]))
            graph[edge[1]].append((edge[0], edge[2]))
        return graph
    @staticmethod
    def findmst(nodes, edges):
        graph = Prims_Algorithm.buildGraph(edges, nodes)
        
        min_heap = []
        mstset = [False]*(nodes+1)
        distance = [math.inf]*(nodes+1)
        parent = [-1]*(nodes+1)
        distance[1] = 0
        parent[1] = -1
        heappush(min_heap, (distance[1], 1 ))
        while min_heap :
            curr_distance , curr_node = heappop(min_heap)
            if mstset[curr_node] :
                continue
            mstset[curr_node] = True
            for nbrpair in graph[curr_node]:
                nbrnode = nbrpair[0]
                nbrdistance = nbrpair[1]
                if not mstset[nbrnode] and nbrdistance < distance[nbrnode]:
                    distance[nbrnode] = nbrdistance
                    parent[nbrnode] = curr_node
                    heappush(min_heap, (distance[nbrnode], nbrnode))
        
        mincost = 0
        for i in range(1,len(distance)):
            mincost += distance[i]
        return mincost
            
        
if __name__ == '__main__':
    nodes = 9
    edges = [[1, 2, 1], [1, 3, 6], [2, 4, 3], [2, 6, 5], [3, 5, 2], [3, 6, 8], [4, 8, 7], [5, 6, 3], [5, 7, 2], [7, 8, 9], [7, 9, 4], [8, 9, 3]]
    cost = Prims_Algorithm.findmst(nodes, edges)
    print(cost)