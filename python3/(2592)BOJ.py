# https://www.acmicpc.net/problem/2592

# 최빈값(mode)를 구하기 위한 모듈 import
from collections import Counter

l = []
sum = 0

for _ in range(10):
    n = int(input())
    sum += n
    l.append(n)

mean = sum // 10
cnt = Counter(l)
mode = cnt.most_common(1)
print(mean)
print(mode[0][0])
