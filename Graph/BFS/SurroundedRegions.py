from collections import deque
class Solution:
    def solve(board):
        """
        Do not return anything, modify board in-place instead.
        """
        def solve(board):
            rows = len(board)
            cols = len(board[0])
            q = deque()
            visited  = [[False for _ in range(cols)] for _ in range(rows)]
                  
            for i in range(rows):
                for j in range(cols):
                    if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                        if board[i][j] == "O":
                            q.append((i,j))
                            visited[i][j]  = True
                            
                                    
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while q:
                row , col  = q.popleft()
                for direction in directions:
                    r = row + direction[0]
                    c = col + direction[1]
                    if r > 0 and r < rows and c >0 and c < cols and not visited[r][c] and board[r][c] == "O":
                        
                        visited[r][c]  = True
                    
                        q.append((r,c))

            for i in range(rows):
                for j in range(cols):
                    if not visited[i][j]:
                        board[i][j] = "X"
            return board
        solve(board)