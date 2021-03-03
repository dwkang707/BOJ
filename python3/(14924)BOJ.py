# https://www.acmicpc.net/problem/14924

S, T, D = map(int, input().split())
h = D // (2 * S)
result = h * T
print(result)
