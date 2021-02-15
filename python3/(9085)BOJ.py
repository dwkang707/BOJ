# https://www.acmicpc.net/problem/9085

T = int(input())
for i in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    print(sum(array))
