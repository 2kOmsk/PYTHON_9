class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in row]) for row in self.data])
    
    def __add__(self, neself):
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + neself.data[i][j])
            result.append(row)
        return Matrix(result)
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Матрас 1:")
print(matrix1)

print("Матрас 2:")
print(matrix2)

print("Сложение: ")
print(matrix1 + matrix2)