class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != ".":
                    if int(board[i][j]) not in visited:
                        visited.add(int(board[i][j]))
                        # print(visited)
                    else:
                        return False
            visited = set()
                                    
        for j in range(cols):
            for i in range(rows):
                if board[i][j]!=".":
                    if int(board[i][j]) not in visited:
                        visited.add(int(board[i][j]))
                        # print(visited)
                    else:
                        return False
            visited = set()
        block = [0,1,2,3,4,5,6,7,8]
        for b in block:
            for i in range((b//3)*3,((b//3)*3)+3):
                for j in range((b%3)*3,((b%3)*3)+3):
                    if board[i][j]!=".":
                        if int(board[i][j]) not in visited:
                            visited.add(int(board[i][j]))
                            print(i,j)
                            print(visited)
                        else:
                            print("in")
                            return False
            visited = set()
        return True
                    
                    
                    
                                    
    
        
                
        