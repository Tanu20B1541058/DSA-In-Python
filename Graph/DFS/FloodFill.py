class Solution:
    directions= [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(self, row, col, image, oldcolor,color):
        if (row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != oldcolor):
            return
        image[row][col] = color
        
        for direction in self.directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            self.dfs(new_row, new_col, image, oldcolor, color)



    def floodFill(self, image, sr: int, sc: int, color: int) :
        if image[sr][sc] == color :
            return image
        self.dfs(sr, sc, image, image[sr][sc], color)
        return image