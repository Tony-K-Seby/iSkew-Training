n=int(input())
l=[int(input()) for x in range(n)]
c=0
for i in l:
    if i%2==1:
        c+=1
if c==0:
    print('No odd elements are present')
else:
    print('Odd Elements:',c)