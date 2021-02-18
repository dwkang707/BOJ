# https://www.acmicpc.net/problem/10162

T = int(input())
A, B, C = 0, 0, 0
while 0 < T:
    if 300 <= T:
        T -= 300
        A += 1
    elif 60 <= T:
        T -= 60
        B += 1
    elif 10 <= T:
        T -= 10
        C += 1
    else:
        break
if T == 0:
    print(A, B, C)
else:
    print(-1)
