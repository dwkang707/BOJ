# https://www.acmicpc.net/problem/9711

n = int(input())
array = [0, 1]
for i in range(2, 10000 + 1):
        array.append(array[i - 1] + array[i - 2])

for i in range(1, n + 1):
    P, Q = map(int, input().split())
    print('Case #%d: %d' % (i, array[P] % Q))
