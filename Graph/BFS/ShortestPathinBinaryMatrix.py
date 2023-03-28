from collections import deque
class Solution:
    def shortestPathBinaryMatrix(grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] !=0 or grid[rows-1][cols-1] !=0:
            return -1
        directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
        queue = deque()
        queue.append((0,0,0))
        grid[0][0] = 2 

        while queue:
            row, col, d = queue.popleft()
            
            
            if row == rows-1 and col == cols-1:
                return d+1
            for direction in directions:
                new_row, new_col, new_d = row + direction[0], col + direction[1], d+1
                if new_row >= 0 and new_row < rows and new_col > 0 and new_col < cols and grid[new_row][new_col] ==0:
                    
                    queue.append((new_row,new_col,new_d))
                    grid[new_row][new_col] = 2
        return -1
