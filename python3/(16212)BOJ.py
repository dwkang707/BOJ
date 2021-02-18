# https://www.acmicpc.net/problem/16212

N = int(input())
array = list(map(int, input().split()))
array.sort()
for i in array:
    print(i, end=' ')
