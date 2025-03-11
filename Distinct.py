n=int(input())
l=[int(x) for x in input().split()]

if len(l)>len(set(l)):
    print('true')
else:
    print('false')        