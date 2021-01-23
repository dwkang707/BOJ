# https://www.acmicpc.net/problem/3047

l = list(map(int, input().split()))
l.sort()
s = input()
for i in s:
    if i == 'A':
        print(l[0], end=" ")
    elif i == 'B':
        print(l[1], end=" ")
    else:
        print(l[2], end=" ")
