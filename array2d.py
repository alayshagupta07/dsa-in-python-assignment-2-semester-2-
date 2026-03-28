def row_sum(matrix):
    print("\nRow Sum:")
    for i in range(len(matrix)):
        s = 0
        for j in range(len(matrix[0])):
            s += matrix[i][j]
        print("Row", i, "=", s)


def column_sum(matrix):
    print("\nColumn Sum:")
    for j in range(len(matrix[0])):
        s = 0
        for i in range(len(matrix)):
            s += matrix[i][j]
        print("Column", j, "=", s)


def search(matrix, x):
    print("\nSearch Result:")
    found = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == x:
                print("Found at position:", i, j)
                found = True
    if not found:
        print("Not Found")


def transpose(matrix):
    print("\nTranspose:")
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            print(matrix[i][j], end=" ")
        print()


# ----------- DRIVER CODE -----------

# Input
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []
print("Enter matrix:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Output original matrix
print("\nMatrix:")
for row in matrix:
    print(row)

# Operations
row_sum(matrix)
column_sum(matrix)

x = int(input("\nEnter value to search: "))
search(matrix, x)

transpose(matrix)