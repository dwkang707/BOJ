# https://www.acmicpc.net/problem/11726

n = int(input())
array = [0, 1, 2, 3]
# 타일을 직접 그려보면 점화식을 도출할 수 있다.
# n=1 -> 1, n=2 -> 2, n=3 -> 3, n=4 -> 5, n=5 -> 8, ... , n=9 -> 55...
# a2-a1=1, a3-a2=1, a4-a3=2, ... , a9-a8=21...
# an = a(n-1) + a(n-1) - a(n-2) + a(n-2) - a(n-3)
# an = 2 * a(n-1) - a(n-3) => n >= 3
if n <= 3:
    print(array[n] % 10007)
else:
    for i in range(4, n + 1):
        array.append(2 * array[i - 1] - array[i - 3])
    print(array[n] % 10007)
