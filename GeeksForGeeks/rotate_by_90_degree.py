def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]