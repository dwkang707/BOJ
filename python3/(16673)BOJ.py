# https://www.acmicpc.net/problem/16673

C, K, P = map(int, input().split())
num = 0
for n in range(1, C + 1):
    num += K * n + P * n ** 2
print(num)
