total = 0
count = 0
pos = 0
neg = 0
while True:
    x = int(input())
    if x == 0:
        break
    total += x
    count += 1
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
if count > 0:
    avg = total / count
else:
    avg = 0
print(avg)
print(pos)
print(neg)
