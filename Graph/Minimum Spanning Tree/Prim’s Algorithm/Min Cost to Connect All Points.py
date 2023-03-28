from heapq import *
import math
class MinCosttoConnectAllPoints:
    
    def buildGraph(edges, nodes, wells):
        graph = []
        for i in range(nodes + 1):
            graph.append(list())
        for edge in edges:
            graph[edge[0]].append((edge[1], edge[2]))
            graph[edge[1]].append((edge[0], edge[2]))
        for i in range(1,nodes):
            graph[0].append((i, wells[i-1]))
            graph[i].append((0, wells[i-1]))
        return graph
    @staticmethod
    def findmst(nodes, edges, wells):
        graph = MinCosttoConnectAllPoints.buildGraph(edges, nodes, wells)
        
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
        for i in range(0,len(distance)):
            mincost += distance[i]
        return mincost
            
        
if __name__ == '__main__':
    nodes = 5
    wells = [1, 4, 6, 5, 3]
    edges = [[1, 2, 3], [1, 4, 6], [1, 5, 2], [2, 4, 5], [3, 5, 7]]
    cost = MinCosttoConnectAllPoints.findmst(nodes, edges, wells)
    print(cost)