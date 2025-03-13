l=[int(x) for x in input().split(',')]
price=float('inf')
profit=0
for i in l:
    if i<price:
        price=i
    elif i-price>profit:
        profit=i-price
print(profit)