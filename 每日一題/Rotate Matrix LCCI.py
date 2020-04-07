class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        #沿著中線水平翻轉
        '''
         1  2  3  4
         5  6  7  8
         ----------
         7  8  9 10
        11 12 13 14
        '''
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        #主對角線翻轉
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
