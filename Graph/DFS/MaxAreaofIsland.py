class Solution:
    directions= [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] !=1:
            return 0
        c = 1
        grid[x][y] = 2
        for direction in self.directions: 
            new_row = x + direction[0]
            new_col = y + direction[1] 
            c = c + self.dfs(new_row, new_col, grid)
        return c   
                
    def maxAreaOfIsland(self, grid) -> int:
        Maxcount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = self.dfs(i, j, grid) 
                    Maxcount = max(Maxcount, count)
        return Maxcount