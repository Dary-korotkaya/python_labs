def check_positive_elements(matrix):
    # Переменная, которая будет показывать, есть ли положительные элементы в каждой строке
    all_positive = True

    # Проверяем каждую строку в матрице
    for row in matrix:
        # Переменная, которая показывает, есть ли хотя бы один положительный элемент в текущей строке
        row_has_positive = False

        # Проверяем каждый элемент в текущей строке
        for element in row:
            if element > 0:
                row_has_positive = True
                # Если найден положительный элемент, выходим из цикла
                break

        # Если в текущей строке нет положительных элементов, устанавливаем флаг all_positive в False
        if not row_has_positive:
            all_positive = False
        else:
            # Если в текущей строке есть положительный элемент, меняем знаки всех элементов
            # на обратные, используя list comprehension
            row[:] = [-x for x in row]

    return all_positive, matrix


# Примеры матриц
matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]  # Эта матрица не имеет положительных элементов в первой строке

# Проверка с первой матрицей
result1, modified_matrix1 = check_positive_elements(matrix1)

if result1:
    print("В каждой строке первой матрицы есть хотя бы один положительный элемент.")
    print("Модифицированная матрица с обратными знаками элементов:")
    for row in modified_matrix1:
        print(row)
else:
    print("Не в каждой строке первой матрицы есть хотя бы один положительный элемент.")

# Проверка со второй матрицей
result2, modified_matrix2 = check_positive_elements(matrix2)

if result2:
    print("В каждой строке второй матрицы есть хотя бы один положительный элемент.")
    print("Модифицированная матрица с обратными знаками элементов:")
    for row in modified_matrix2:
        print(row)
else:
    print("Не в каждой строке второй матрицы есть хотя бы один положительный элемент.")
