class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        t = m * n
        l = 0
        r = t - 1
        while l <= r:
            m = (l+r) // 2
            i = m // n
            j = m % n

            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m - 1
            else:
                l = m + 1
        return False
    
#time: O(log (m*n) )    space: O(1)