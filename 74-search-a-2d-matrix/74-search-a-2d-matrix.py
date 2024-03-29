class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            elif matrix[i][-1] == target:
                return True
            else:
                l = 0
                r = len(matrix[i])-1
                while l<=r:
                    mid = l + (r-l)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        r = mid-1
                    else:
                        l = mid+1
        return False


        