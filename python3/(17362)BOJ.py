# https://www.acmicpc.net/problem/17362

n = int(input())
# 첫번째와 다섯번째는 8로 나누면 나머지가 무조건 각각 1과 5가 나온다.
# 두번째는 8로 나누면 나머지가 2 아니면 0이다.
# 세번째는 8로 나누면 나머지가 3 아니면 7이다.
# 네번째는 8로 나누면 나머지가 4 아니면 6이다.
if 1 <= n % 8 and n % 8 <= 5:
    print(n % 8)
elif n % 8 == 6:
    print(4)
elif n % 8 == 7:
    print(3)
elif n % 8 == 0:
    print(2)
