# https://www.acmicpc.net/problem/5355

n = int(input())
for _ in range(n):
    l = list(input().split())
    l[0] = float(l[0])
    for i in range(1, len(l)):
        if l[i] == '@':
            l[0] *= 3
        elif l[i] == '%':
            l[0] += 5
        elif l[i] == '#':
            l[0] -= 7
    print('%.2f' % l[0])
