class Matrix:
    matrix: list

    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        mystr = '\n'.join(['\t'.join([str(x)
                    for x in self.matrix[i]])
                        for i in range(len(self.matrix))])
        return mystr

    def __add__(self, other):
        newMatrix = [[self.matrix[i][j] + other.matrix[i][j]  # Складываем
                        for j in range(len(self.matrix[i]))]  # j
                            for i in range(len(self.matrix))]  # i
        return Matrix(newMatrix)


data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]]
mat = Matrix(data)
print(mat)
print('Теперь сложим матрицу саму с собой и выведем на печать')
new_mat = mat + mat
print(new_mat)
