# https://www.acmicpc.net/problem/1427

import sys
N = sys.stdin.readline().rstrip()
array = list(N)
result = sorted(array, reverse=True)
for i in result:
    print(i, end='')
