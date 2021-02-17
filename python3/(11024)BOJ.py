# https://www.acmicpc.net/problem/11024

T = int(input())
for i in range(T):
    array = list(map(int, input().split()))
    result = sum(array)
    print(result)
