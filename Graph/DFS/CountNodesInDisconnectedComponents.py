class CountNodesInDisconnectedComponents:
    
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
                c += CountNodesInDisconnectedComponents.dfs(nbr,visited,graph)
        return c
    
    
    def disconnectedComponents(v, edges):
        graph = CountNodesInDisconnectedComponents.buildGraph(v, edges)
        visited = [False]*(v+1)
        connectedCount = []
        for i in range(1,v+1):
            if not visited[i]:
                c = CountNodesInDisconnectedComponents.dfs(i, visited, graph)
                connectedCount.append(c)
        return connectedCount
    
if __name__ == '__main__':
    v = 5
    edges = [[1, 2], [1, 3], [1,4]]
    print(CountNodesInDisconnectedComponents.disconnectedComponents(v, edges))
    
    