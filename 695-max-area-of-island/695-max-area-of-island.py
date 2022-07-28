class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        def bfs(a,b, ar):
            visited.add((a,b))
            q = collections.deque()
            q.append((a,b))
            while q:
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0, -1]]
                for a,b in directions:
                    row = r+a
                    col = c+b
                    if (row in range(rows) and
                       col in range(columns) and 
                       grid[row][col]==1 and 
                       (row, col) not in visited):
                        q.append((row,col))
                        visited.add((row, col))
                        ar += 1
            return ar
                        
        
        maxarea = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    are = 1
                    area = bfs(i, j, are)
                    islands = islands+1
                    maxarea = max(maxarea, area)
        return maxarea
                    
        