# https://www.acmicpc.net/problem/16561

# n=9 -> 1, n=12 -> 3, n=15 -> 6, n=18 -> 10, ...
# 1, 3, 6, 10, ... -> 처음에 2 다음에 3 그다음에 4 순으로 더해진다.
n = int(input())
num = 1
count = 2
for i in range(9, n, 3):
    num += count
    count += 1
print(num)
