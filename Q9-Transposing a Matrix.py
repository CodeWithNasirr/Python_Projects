# Input
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Output
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

def flatten_matrix(matrix):
    return[[row[i] for row in matrix] for i in range(len(matrix[1]))]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

x=flatten_matrix(matrix)
print(x)