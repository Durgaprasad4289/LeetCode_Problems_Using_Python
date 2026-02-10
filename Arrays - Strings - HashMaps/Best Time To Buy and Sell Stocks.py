
prices = [7,1,5,3,6,4]
min_price=float('inf')
profit=0

for i in prices:
    if min_price>i:
        min_price=i
    if i-min_price>profit:
        profit=i-min_price
print(profit)