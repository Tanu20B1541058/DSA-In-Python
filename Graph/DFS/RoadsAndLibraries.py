class RoadsAndLibraries:
    
    def buildGraph(v,edges):
        graph = [[] for _ in range(v+1)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    
    @staticmethod
    def dfs(node, visited, graph):
        visited[node] = True
        c = 1
        for nbr in graph[node]:
            if not visited[nbr]:
                c += RoadsAndLibraries.dfs(nbr,visited,graph)
        return c
    
    
    def roadsAndLibraries(n, c_lib, c_road, cities):
        graph = RoadsAndLibraries.buildGraph(n, cities)
        visited = [False]*(n+1)
        connectedCount = []
        for i in range(1,n+1):
            if not visited[i]:
                c = RoadsAndLibraries.dfs(i, visited, graph)
                connectedCount.append(c)
        print(connectedCount)
        cost = 0
        for cityCount in connectedCount:
            cost += min((c_lib + (cityCount - 1) * c_road), (cityCount * c_lib))

        return cost

    