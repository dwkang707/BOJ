# https://www.acmicpc.net/problem/10474

while True:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        print(a // b, a % b, "/", b)
    else:
        break
