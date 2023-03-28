v = 5
edges = [[1, 2], [1, 4], [1, 5], [2, 3], [2, 5], [3, 5]]
def matrix(v,edges):
    mat=[[0 for i in range(v+1)]for j in range(v+1)]
    for edge in edges:
        mat[edge[0]][edge[1]]=1
        mat[edge[1]][edge[0]]=1
    return mat 
print(matrix(v,edges))