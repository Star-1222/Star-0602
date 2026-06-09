a, n = map(int, input().split())
total = int(str(a) * n)  # R(n)
for i in range(1, n):
    total -= int(str(a) * i)
print(total)
