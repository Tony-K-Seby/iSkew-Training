n=int(input())
flag=0
for i in range(2,int(n**.5)+1):
    if n%i==0:
        flag=1
if flag==0:
    print(n,'is a prime number')
else:
    print(n,'is not a prime number')