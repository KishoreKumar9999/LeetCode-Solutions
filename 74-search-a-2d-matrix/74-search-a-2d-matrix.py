# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for i in range(len(matrix)):
#             if matrix[i][-1] < target:
#                 continue
#             elif matrix[i][-1] == target:
#                 return True
#             else:
#                 l = 0
#                 r = len(matrix[i])-1
#                 while l<=r:
#                     mid = l + (r-l)//2
#                     if matrix[i][mid] == target:
#                         return True
#                     elif matrix[i][mid] > target:
#                         r = mid-1
#                     else:
#                         l = mid+1
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        