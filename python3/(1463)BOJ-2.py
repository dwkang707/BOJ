# https://www.acmicpc.net/problem/1463

N = int(input())

# DP table 초기화
d = [0] * 1000001

# Dynamic programming 진행(Bottom-up)
for i in range(2, N + 1):
    # 함수의 호출 횟수를 구하는 문제이므로 +1을 해주어야 한다.
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
print(d[N])
