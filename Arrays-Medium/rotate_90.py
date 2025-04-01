#rotate matrix
# Input:
#  [[1,2,3],[4,5,6],[7,8,9]]

# Output
# : [[7,4,1],[8,5,2],[9,6,3]]

# Explanation:
#  Rotate the matrix simply by 90 degree clockwise and return the matrix.


def rotate_matrix(matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
             matrix[i].reverse()
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = rotate_matrix(matrix)
print(sol)
