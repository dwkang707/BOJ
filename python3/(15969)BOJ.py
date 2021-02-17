# https://www.acmicpc.net/problem/15969

N = int(input())
array = list(map(int, input().split()))
min_score = min(array)
max_score = max(array)
result = max_score - min_score
print(result)
