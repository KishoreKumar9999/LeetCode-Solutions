class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        # Phase 1: Converting the border O's into T's.
        def dfs(r, c):
            if (r<0 or
            c<0 or
            r == rows or
            c == cols or 
            board[r][c] != "O"):
                return 
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r in [0, rows-1] or c in [0, cols-1])):
                    dfs(r,c)
        
        # Phase 2: Change O's to X's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Phase 3: Change T's to O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        pass
        
            
            