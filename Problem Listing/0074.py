# https://leetcode.com/problems/search-a-2d-matrix/
# 49 ms, 17.02 MB

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchRow(mid):
            left, row_mid, right = 0, 0, len(matrix[0])-1
            while left <= right:
                row_mid = (left + right) // 2
                if matrix[mid][row_mid] == target:
                    return True
                elif matrix[mid][row_mid] < target:
                    left = row_mid + 1
                else:
                    right = row_mid - 1
            return False
        
        top, mid, bottom = 0, 0, len(matrix)-1
        
        while top <= bottom:
            mid = (bottom + top) // 2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0])-1]:
                return searchRow(mid)
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
        return False

        
