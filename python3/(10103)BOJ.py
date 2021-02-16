# https://www.acmicpc.net/problem/10103

n = int(input())
# 기본 점수 100점
chang, sang = 100, 100
for i in range(n):
    # a: 창영이의 주사위 수, b: 상덕이의 주사위의 수
    a, b = map(int, input().split())
    if a < b:
        chang -= b
    elif a > b:
        sang -= a
print(chang)
print(sang)
