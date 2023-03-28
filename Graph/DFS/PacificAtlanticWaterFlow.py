
class Solution:
    directions= [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(self, x, y, prev, heights ,ocean):
        if (x < 0 or x == len(heights) or y < 0 or  y == len(heights[0])) or (x,y) in ocean or heights[x][y] < prev:
            return
        
        ocean.add((x,y))
        
        
        for direction in self.directions: 
            new_row = x + direction[0]
            new_col = y + direction[1] 
            self.dfs(new_row, new_col, heights[x][y], heights, ocean)
        
                
    def pacificAtlantic(self, heights):
        x = len(heights)
        y = len(heights[0])
        pacific = set()
        atlantic = set()
        
        for col in range(y):
            self.dfs(0,col,0,heights,pacific)
            self.dfs(x-1,col , 0,heights,atlantic)
        for row in range(0,x):
            self.dfs(row,0,0,heights,pacific)
            self.dfs(row,y-1 , 0,heights,atlantic)
        return list(pacific.intersection(atlantic))