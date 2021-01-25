# https://www.acmicpc.net/problem/1547

m = int(input())
cup = [1, 2, 3]
for _ in range(m):
    x, y = map(int, input().split())
    i, j = cup.index(x), cup.index(y)
    cup[i], cup[j] = y, x
print(cup[0])
