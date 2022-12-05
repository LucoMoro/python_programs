matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][2] = 20
print(matrix[0][2])
print(matrix)

for row in matrix:
    for item in row:
        print(item)