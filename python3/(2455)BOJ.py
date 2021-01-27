# https://www.acmicpc.net/problem/2455

# A: 내린 사람 수, B: 탄 사람 수, C: 열차 내 사람 수, max: 가장 많이 탔었던 사람 수
max = 0
C = 0
for _ in range(4):
    A, B = map(int, input().split())
    C += (B - A)
    if max < C:
        max = C
print(max)
