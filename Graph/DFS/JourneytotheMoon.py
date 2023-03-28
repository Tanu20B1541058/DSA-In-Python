import math
import os
import random
import re
import sys
sys.setrecursionlimit(6000)
#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    def buildGraph(v,edges):
        graph = [[] for _ in range(v)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    def dfs(node, visited, graph):
        visited[node] = True
        c = 1
        for nbr in graph[node]:
            if not visited[nbr]:
                c += dfs(nbr,visited,graph)
        return c
    
    graph = buildGraph(n, astronaut)
    visited = [False]*(n+1)
    connectedCount = []
    for i in range(n):
        if not visited[i]:
            c = dfs(i, visited, graph)
            connectedCount.append(c)
    ans = 0
    l = len(connectedCount)
    total= n*(n-1)//2
    same=0
    for c in connectedCount:
        same=same+c*(c - 1)//2
    print(total-same)
    return (total-same)