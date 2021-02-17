# https://www.acmicpc.net/problem/9325

T = int(input())
for i in range(T):
    s = int(input())
    n = int(input())
    price = s
    for j in range(n):
        q, p = map(int, input().split())
        price += q * p
    print(price)
