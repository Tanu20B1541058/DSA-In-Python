class DSU:
    def union(u,v,parent):
        pu=DSU.find(u,parent)
        pv=DSU.find(v,parent)
        if pu!=pv:
            parent[pv]=pu


    def find(node,parent):
        if parent[node]==node:
            return node
        return DSU.find(parent[node],parent)

    def connectedComponenets(n,edges):
        parent=[]*(n)
        for i in range(n):
            parent.append(i) 
        for edge in edges:
            DSU.union(edge[0],edge[1],parent)
        for i in range(n):
            print(parent[i],"is parent",i)
    

if __name__ == '__main__':
    n=9
    edges=[[0,1], [1,2], [1,3], [1,4], [2,4], [5,6], [6,7], [7,8]]
    DSU.connectedComponenets(n,edges)