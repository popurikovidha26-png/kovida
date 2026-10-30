# Creating two matrices using nested lists
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Displaying matrices
print("Matrix A:")
for row in A:
    print(row)

print("Matrix B:")
for row in B:
    print(row)

# Matrix Addition
print("Matrix Addition:")
for i in range(2):
    for j in range(2):
        print(A[i][j] + B[i][j], end=" ")
    print()

# Matrix Subtraction
print("Matrix Subtraction:")
for i in range(2):
    for j in range(2):
        print(A[i][j] - B[i][j], end=" ")
    print()

# Matrix Multiplication
print("Matrix Multiplication:")
for i in range(2):
    for j in range(2):
        total = 0
        for k in range(2):
            total += A[i][k] * B[k][j]
        print(total, end=" ")
    print()

# Transpose of Matrix A
print("Transpose of Matrix A:")
for i in range(2):
    for j in range(2):
        print(A[j][i], end=" ")
    print()
