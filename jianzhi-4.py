def findNumInMatrix(matrix, num):
    m, n = len(matrix), len(matrix[0])
    i = 0
    j = n-1
    while i < m and j > -1:
        if matrix[i][j] == num:
            return True
        elif matrix[i][j] > num:
            j -= 1
        else:
            i += 1
    return False


print(findNumInMatrix(
    [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ], 7
))
