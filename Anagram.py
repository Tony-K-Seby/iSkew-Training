s=input()
t=input()
ds={}
dt={}
for i in s:
    ds[i]=ds.get(i,0)+1
for i in t:
    dt[i]=dt.get(i,0)+1
if ds==dt:
    print('true')
else:
    print('false')    