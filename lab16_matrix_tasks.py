import numpy as np

# КРОК 1: Сума та кількість додатних елементів над головною діагоналлю
N = 5
np.random.seed(0)
A = np.random.randint(-10, 11, (N, N))

positive_sum = 0
positive_count = 0
for i in range(N):
    for j in range(i+1, N):
        if A[i][j] > 0:
            positive_sum += A[i][j]
            positive_count += 1

print("КРОК 1: Матриця A:")
print(A)
print("Сума додатних над головною діагоналлю:", positive_sum)
print("Кількість додатних над головною діагоналлю:", positive_count)
print("-" * 50)

# КРОК 2: Заміна макс/мін елементів з початком/кінцем рядка
N, M = 4, 6
np.random.seed(1)
B = np.random.randint(1, 21, (N, M))
B_modified = B.copy()

for i in range(N):
    row = B_modified[i]
    min_index = np.argmin(row)
    max_index = np.argmax(row)
    row[-1], row[min_index] = row[min_index], row[-1]
    if max_index == M - 1:
        max_index = min_index
    row[0], row[max_index] = row[max_index], row[0]

print("КРОК 2: Оригінальна матриця B:")
print(B)
print("Змінена матриця B:")
print(B_modified)
print("-" * 50)

# КРОК 3: Перевірка на магічний квадрат
magic_candidate = np.array([
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
])
target_sum = sum(magic_candidate[0])
is_magic = True
for row in magic_candidate:
    if sum(row) != target_sum:
        is_magic = False
        break
if is_magic:
    for col in range(magic_candidate.shape[1]):
        if sum(magic_candidate[:, col]) != target_sum:
            is_magic = False
            break
if is_magic:
    if sum(magic_candidate.diagonal()) != target_sum or        sum(np.fliplr(magic_candidate).diagonal()) != target_sum:
        is_magic = False

print("КРОК 3: Магічний квадрат:")
print(magic_candidate)
print("Є магічним квадратом?" , is_magic)
print("-" * 50)

# КРОК 4: Обмін першого і останнього стовпців
np.random.seed(3)
N = 4
A_rect = np.random.randint(1, 21, (N, N))
A_swapped = A_rect.copy()
A_swapped[:, [0, -1]] = A_swapped[:, [-1, 0]]

print("КРОК 4: Оригінальна матриця A:")
print(A_rect)
print("Після обміну 1-го і останнього стовпців:")
print(A_swapped)
print("-" * 50)

# КРОК 5: Симетрія відносно головної діагоналі
symmetric_matrix = np.array([
    [1, 2, 3, 4],
    [2, 5, 6, 7],
    [3, 6, 8, 9],
    [4, 7, 9, 10]
])
is_symmetric = np.array_equal(symmetric_matrix, symmetric_matrix.T)

print("КРОК 5: Кандидат на симетричну матрицю:")
print(symmetric_matrix)
print("Є симетричною?", is_symmetric)
print("-" * 50)

# КРОК 6: Рядки з найменшою і найбільшою сумою
np.random.seed(6)
matrix = np.random.randint(-10, 20, (5, 6))
row_sums = matrix.sum(axis=1)
min_row_index = np.argmin(row_sums)
max_row_index = np.argmax(row_sums)
min_row = matrix[min_row_index]
max_row = matrix[max_row_index]
min_sum = row_sums[min_row_index]
max_sum = row_sums[max_row_index]

print("КРОК 6: Матриця:")
print(matrix)
print("Рядок з найменшою сумою:", min_row.tolist(), "Сума:", int(min_sum))
print("Рядок з найбільшою сумою:", max_row.tolist(), "Сума:", int(max_sum))
