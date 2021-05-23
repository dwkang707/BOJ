# https://www.acmicpc.net/problem/20001

import sys

s = sys.stdin.readline().strip()
score = 0

while True:
    s = sys.stdin.readline().strip()

    if s == '고무오리 디버깅 끝':
        break

    if s == '고무오리':
        if score == 0:
            score += 2
        else:
            score -= 1
    else:
        score += 1

if score == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")
