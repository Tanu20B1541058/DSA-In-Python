def solveNQueens(n):
        cols,diagonals,anti_diagonals=[],[],[]
        board=[['.']*n for i in range(n)]
        ans=[]
        

        def solve(row,cols,diagonals,anti_diagonals,board,ans):
            if row== len(board):
                ans.append(["".join(i) for i in board])

                
                return
            for col in range(len(board)):
                curr_diag=row-col
                curr_ant_diag=row+col

                if (col in cols ) or (curr_diag in diagonals) or (curr_ant_diag in anti_diagonals):
                    continue
                cols.append(col)
                diagonals.append(curr_diag)
                anti_diagonals.append(curr_ant_diag)
                board[row][col]='Q'

                solve(row+1,cols,diagonals,anti_diagonals,board,ans)

                cols.pop()
                diagonals.pop()
                anti_diagonals.pop()
                board[row][col]='.'
        solve(0,cols,diagonals,anti_diagonals,board,ans)
        return ans
n=4
print(solveNQueens(n))
