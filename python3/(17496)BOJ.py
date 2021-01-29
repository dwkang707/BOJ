# https://www.acmicpc.net/problem/17496

N, T, C, P = map(int, input().split())
count = 0
i = 1
while True:
    # 수확가능한 날짜가 등차수열을 이룬다.
    if N >= T * i + 1:
        count += 1
        i += 1
    else:
        break
result = count * C * P
print(result)
