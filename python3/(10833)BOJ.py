# https://www.acmicpc.net/problem/10833

T = int(input())
sum = 0
for _ in range(T):
    A, B = map(int, input().split())
    sum += B % A
print(sum)
