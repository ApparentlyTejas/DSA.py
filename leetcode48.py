class solution:
    def rotateImage(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        #Transpose
        for i in range(n):
            for j in range(i+1 , n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix [i][j]
        #reflection 
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

#time = O(n^2)
#space = O(1)