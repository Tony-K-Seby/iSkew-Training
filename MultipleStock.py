l=[int(x) for x in input().split(',')]
profit=0
for i in range(1,len(l)):
    if l[i]>l[i-1]:
        profit+=l[i]-l[i-1]
print(profit)