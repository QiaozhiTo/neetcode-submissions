class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            m = l + ((r-l)//2)
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                l1, r1 = 0, len(matrix[m])-1
                while l1 <= r1:
                    m1 = l1 + ((r1-l1)//2)
                    if matrix[m][m1] > target:
                        r1 = m1 -1
                    elif matrix[m][m1] < target:
                        l1 = m1 + 1
                    else:
                        return True
                return False
        return False