# https://www.acmicpc.net/problem/19946

N = int(input())
dp = [0] * 65
# 규칙을 확인해보면
# (2^64 - 1) * 2^0 = 2^64 - 2^0
# (2^63 - 1) * 2^1 = 2^64 - 2^1
# (2^62 - 1) * 2^2 = 2^64 - 2^2
for i in range(0, 65):
    dp[64 - i] = 2 ** 64 - 2 ** i
    
low = 0
high = 64
mid = (high + low) // 2
# 입력한 값이 리스트에 항상 존재하며 정렬된 상태이므로 binary-search를 통해 인덱스 검색
while low <= high:
    if dp[mid] == N:
        print(mid)
        break
    elif dp[mid] > N:
        high = mid - 1
        mid = (low + high) // 2
    else:
        low = mid + 1
        mid = (low + high) // 2
