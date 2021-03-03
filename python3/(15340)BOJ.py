# https://www.acmicpc.net/problem/15340

while True:
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        break
    else:
        print(min(c * 30 + d * 40, c * 35 + d * 30, c * 40 + d * 20))
