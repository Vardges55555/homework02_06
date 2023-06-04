"""Write a program that rotates a matrix by 180 degrees."""

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

rotated_matrix = []
for row in reversed(matrix):
    rotated_row = list(reversed(row))
    rotated_matrix.append(rotated_row)

for elm in rotated_matrix:
    print(elm)
    
