n=int(input())
l=[int(x) for x in input().split()]
t=int(input())
left, right = 0, len(l)-1

while left<right:
    sum = l[left]+l[right]
    if sum == t:
        print('Yes')
        exit()
    elif sum < t: 
        left += 1
    else:
        right -= 1
print('No')