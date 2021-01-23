# https://www.acmicpc.net/problem/14912

n, d = map(int, input().split())
count = 0
for i in range(1, n + 1):
    while i != 0:
        if i % 10 == d:
            count += 1
        i = i // 10
print(count)
