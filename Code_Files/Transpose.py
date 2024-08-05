def get_matrix_input(rows, cols):
    """Function to input matrix elements."""
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i+1}, {j+1}]: "))
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """Function to print the matrix."""
    for row in matrix:
        print(" ".join(map(str, row)))

def transpose_matrix(matrix):
    """Function to compute the transpose of the matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)
    return transpose

# Main program
# Get matrix dimensions
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Get matrix elements
matrix = get_matrix_input(rows, cols)

# Compute the transpose
transpose = transpose_matrix(matrix)

# Display the original matrix
print("\nOriginal Matrix:")
print_matrix(matrix)

# Display the transpose of the matrix
print("\nTranspose of the Matrix:")
print_matrix(transpose)
