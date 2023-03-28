class Solution:
    directions= [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(self, row, col, grid):
        if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1'):
            return
        grid[row][col] = '2'

        for direction in self.directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            self.dfs(new_row, new_col, grid)
    
    def numIslands(self, grid) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    count += 1
        return count