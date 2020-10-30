class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result_str = ''
        for i in self.matrix:
            result_str += '\t'.join(map(str, i)) + '\n'
        return result_str

    def __add__(self, other):
        result_matrix = [None] * len(self.matrix)
        for i in range(len(self.matrix)):
            result_matrix[i] = [None] * len(self.matrix[i])
            for j in range(len(self.matrix[i])):
                result_matrix[i][j] = self.matrix[i][j]+other.matrix[i][j]
        return Matrix(result_matrix)


m_1 = Matrix([[1, 2], [3, 4], [5, 6]])
m_2 = Matrix([[1, 2], [3, 4], [5, 6]])
print(m_1+m_2)
