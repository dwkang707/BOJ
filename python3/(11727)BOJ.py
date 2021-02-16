# https://www.acmicpc.net/problem/11727

n = int(input())
array = [0, 1, 3]
# 타일을 직접 그려보면 점화식을 도출할 수 있다.
# n=1 -> 1, n=2 -> 3, n=3 -> 5, n=4 -> 11, n=5 -> 21, ... , n=8 -> 171...
# an = 2 * a(n-2) + a(n-1) => n >= 3
if n >= 3:
    for i in range(3, n + 1):
        array.append(2 * array[i - 2] + array[i - 1])
print(array[n] % 10007)
