def get_matrix(n, m, value):
    matrix = []
    for a in range(n):
        matrix.append([])
        for b in range(m):
            matrix[a].append(value)
    return matrix

result1 = get_matrix(3, 2, 5)
result2 = get_matrix(3, 6, 22)
result3 = get_matrix(4, 4, 38)
print(result1)
print(result2)
print(result3)