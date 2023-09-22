class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        c=len(matrix[0])
        for i in range(len(matrix)):
            for j in range(c):
                if(matrix[i][j]==target):
                    return True
        else:
            return False
            