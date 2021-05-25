# https://www.acmicpc.net/problem/9093

import sys
n = int(input())
for i in range(n):
    s = sys.stdin.readline().strip()
    s_l = list(s.split())
    for j in s_l:
        print(j[::-1], end=' ') # [::-1]은 문자열을 뒤집어서 출력할 수 있다.
