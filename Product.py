n=int(input())
l=[float(input()) for x in range(n)]
p=1
for i in l:
    p*=i
print(f'The product of the numbers is: {p:.2f}')