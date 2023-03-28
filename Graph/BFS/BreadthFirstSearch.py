from collections import deque

class BreadthFirstSearch:
    
    def build_graph(v, edges):
        graph = [[] for i in range(v + 1)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    @staticmethod
    def print_graph(v, edges):
        graph = BreadthFirstSearch.build_graph(v, edges)
        for i in range(1, v + 1):
            print(i, end = " : ")
            for nbr in graph[i]:
                print(nbr, end = " ")
            print()

    def breadthFirstSearch(v, edges, src):
        graph = BreadthFirstSearch.build_graph(v, edges)

        visited = [False] * (v+1)
        queue = deque()
        queue.append(src)
        visited[src] = True

        bfs = []

        while queue:
            node = queue.popleft()
            bfs.append(node)
            for nbr in graph[node]:
                if not visited[nbr]:
                    queue.append(nbr)
                    visited[nbr] = True
        
        return bfs

if __name__ == '__main__':
    v = 5
    edges = [[1, 2], [1, 4], [1, 5], [2, 3], [2, 5], [3, 5]]
    BreadthFirstSearch.print_graph(v, edges)
    print(BreadthFirstSearch.breadthFirstSearch(v, edges, 1))