# https://www.acmicpc.net/problem/14913

a, d, k = map(int, input().split())
# 일반항 = 공차(d) * n - (공차(d) - 초항(a))
n = (k + d - a) / d
val = int(n)
# n과 val이 같으면 k가 공차수열에 포함됨, (k - a) / d < 0인 경우 등차수열에 포함되지 않음.
if n != val or (k - a) / d < 0:
    print("X")
else:
    print(val)
