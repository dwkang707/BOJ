# https://www.acmicpc.net/problem/1247

import sys

for _ in range(3):
    # input()으로 입력시 시간초과 발생하여 sys.stdin.readline() 사용
    N = int(sys.stdin.readline())
    sum = 0
    for _ in range(N):
        val = int(sys.stdin.readline())
        sum += val
    if sum > 0:
        print("+")
    elif sum == 0:
        print(0)
    else:
        print("-")
