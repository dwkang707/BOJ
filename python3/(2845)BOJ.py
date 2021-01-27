# https://www.acmicpc.net/problem/2845

L, P = map(int, input().split())
l = list(map(int, input().split()))
area = L * P
for i in range(len(l)):
    print(l[i] - area, end=" ")
