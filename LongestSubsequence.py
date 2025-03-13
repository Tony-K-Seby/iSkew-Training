n=int(input())
s=[int(x) for x in input().split()]
long=[]
current=[s[0]]

for i in range(1,n):    
    if s[i]>s[i-1]:
        current.append(s[i])
    else:
        if len(current)>len(long):
            long=current
        current=[s[i]]

if len(current)>len(long):
    long=current
print(*long)