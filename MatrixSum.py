rows, cols = map(int, input().split())

mat1 = [list(map(int, input().split())) for _ in range(rows)]
mat2 = [list(map(int, input().split())) for _ in range(rows)]

print("First Matrix:")
for row in mat1:
    print(*row)
print("Second Matrix:")
for row in mat2:
    print(*row)

print("Sum of the two matrices is:")
for i in range(rows):
    print(*[mat1[i][j] + mat2[i][j] for j in range(cols)])