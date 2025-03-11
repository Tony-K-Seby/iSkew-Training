p=input()
c=0
a=0
for i in p:
    if i in 'CU' and a==0:
        c+=1
    elif i in 'RL':
        a+=1
    else:
        a-=1
print(c)