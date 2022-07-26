class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        islands = 0
        r, c = len(grid), len(grid[0])
        def bfs(a, b):
            q = collections.deque()
            visited.add((a,b))
            q.append((a,b))
            
            while q:
                directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
                row, col = q.popleft()
                for h,v in directions:
                    rows = row+h
                    cols = col+v
                    if (rows in range(r) and 
                    cols in range(c) and 
                    grid[rows][cols] == "1" and 
                    (rows, cols) not in visited):
                        q.append((rows, cols))
                        visited.add((rows,cols))
                    
                
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands = islands+1
        return islands