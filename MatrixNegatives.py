r=int(input())
c=int(input())
matrix=[]
count=0

for i in range(r):
    l=[int(x) for x in input().split()]
    matrix.append(l)
i=0;j=0
while i<r and j<c:
    if matrix[i][j]<0:
        count+=1
        j+=1
    else:
        i+=1
        j=0

print(count)