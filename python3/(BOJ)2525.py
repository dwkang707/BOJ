# https://www.acmicpc.net/problem/2525

A, B = map(int, input().split())
C = int(input())
B += C
H = 0
M = 0
if B >= 60:
    M = B % 60
    H = B // 60
    H += A
    if H >= 24:
        H -= 24
else:
    H, M = A, B
print(H, M)
