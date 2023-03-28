def orangesRotting(grid):
        m= len(grid)
        n= len(grid[0])
        
        q=[]
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):
                    q.append((i,j))      
        
        q.append(None)
        time=0
        
        while(len(q)>1):
            x = q.pop(0)
            if(x==None):
                time+=1
                q.append(None)
                continue
                
            i,j= x[0],x[1]
            
            if( 0<= i-1 < m and grid[i-1][j]==1):
                q.append((i-1,j))
                grid[i-1][j]=2
                
            if(0<= i+1<m and grid[i+1][j]==1):
                q.append((i+1,j))
                grid[i+1][j]=2
                
            if(0<= j-1<n and grid[i][j-1]==1):
                q.append((i,j-1))
                grid[i][j-1]=2
                
            if(0<= j+1<n and grid[i][j+1]==1):
                q.append((i,j+1))
                grid[i][j+1]=2
          
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    return -1
        
        return time
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))          