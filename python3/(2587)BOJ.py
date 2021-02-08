# https://www.acmicpc.net/problem/2587

l = []
sum = 0
for _ in range(5):
    n = int(input())
    sum += n
    l.append(n)
l.sort()
mean = sum // 5
median = l[2]
print(mean)
print(median)
