def zigzagmatrix(matrix):
    res = []
    rows = len(matrix)
    for i in range(rows):
        if i % 2 == 0:
            res.extend(matrix[i])
        else:
            res.extend(matrix[i][::-1])
    return res

row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

# Initialize the matrix outside of the loop
matrix = []
for i in range(row):
    rowdata=list(map(int,input().split()))  # You may want to replace this with actual input if desired
    matrix.append(rowdata)  # Add the row to the matrix

print("Zigzag traversal:", zigzagmatrix(matrix))
