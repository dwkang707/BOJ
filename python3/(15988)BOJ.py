# https://www.acmicpc.net/problem/15988

import sys
T = int(sys.stdin.readline().rstrip())
array = [0, 1, 2, 4]
# 케이스를 작성해보면 점화식을 도출할 수 있다.
# n=1 -> 1, n=2 -> 2, n=3 -> 4, n=4 -> 7, n=5 -> 13, ...
# an = a(n-1) + a(n-2) + a(n-3) -> n >= 4
# 어차피 1000000009로 나눈 나머지를 구하는 것이기 때문에 점화식 계산하면서 바로 1000000009로 나누는 나머지 계산 진행
for i in range(4, 1000000+1):
    array.append((array[i - 1] + array[i - 2] + array[i - 3]) % 1000000009)
for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(array[n])
