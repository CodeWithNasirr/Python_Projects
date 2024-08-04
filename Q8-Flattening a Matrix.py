# Input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Output
[1, 2, 3, 4, 5, 6, 7, 8, 9]


def flatten_matrix(matrix):
    return[num for row in matrix for num in row]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

x=flatten_matrix(matrix)
print(x)