# https://www.acmicpc.net/problem/15624

import sys
n = int(sys.stdin.readline().rstrip())
array = [0, 1]
if n >= 2:
    for i in range(2, n + 1):
        array.append((array[i - 1] + array[i - 2]) % 1000000007)
print(array[n])
