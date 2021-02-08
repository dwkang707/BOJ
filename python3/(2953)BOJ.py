# https://www.acmicpc.net/problem/2953

max = 0
player = 0
scores = []
for i in range(5):
    total = 0
    scores.append(list(map(int, input().split())))
    for j in range(4):
        total += scores[i][j]
    if max < total:
        max = total
        player = i + 1
print(player, max)
