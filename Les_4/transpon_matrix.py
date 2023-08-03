### Функция для транспонирования матрицы ###

matrix_n = [[4, 5, 6], [1, 2, 3]]

def tr_matrix():
    return [[matrix_n[j][i] for j in range(len(matrix_n))] for i in range(len(matrix_n[0]))]

print(matrix_n)
print(tr_matrix())