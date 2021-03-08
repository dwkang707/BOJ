# https://www.acmicpc.net/problem/14652

N, M, K = map(int, input().split())
count = 0
n = K // M
m = K % M
print(n, m)
