# https://www.acmicpc.net/problem/1193

X = int(input())
n = 1
while True:
    if n * (n + 1) // 2 >= X:
        break
    n += 1
a = abs(n * (n + 1) // 2 - X)
if n % 2 == 0:
    print(f'{n - a}/{1 + a}')
else:
    print(f'{1 + a}/{n - a}')
