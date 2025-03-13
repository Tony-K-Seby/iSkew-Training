l=[int(x) for x in input().split(',')]
k=int(input())
l=sorted(l)
res=[]
minunfair=float('inf')
for i in range(len(l)-k+1):
    arr=l[i:i+k]
    unfair=max(arr)-min(arr)
    if unfair<minunfair:
        minunfair=unfair
        res=arr
print(*res)