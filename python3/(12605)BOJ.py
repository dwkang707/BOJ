# https://www.acmicpc.net/problem/12605

N = int(input())
for i in range(1, N + 1):
    string = list(input().split())
    print('Case #%d: ' % i, end='')
    for j in range(len(string)):
        print(string.pop(), end=' ')
    print()
