# https://www.acmicpc.net/problem/10179

n = int(input())
for _ in range(n):
    price = float(input())
    result = round(price * 0.8, 2)
    print('$%.2f' % result)
