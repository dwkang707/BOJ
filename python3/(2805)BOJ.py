# https://www.acmicpc.net/problem/2805

import sys
N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위한 시작점과 끝점 지정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2 # 자르려고 하는 높이
    for x in array:
        # 잘랐을때 나무의 길이 계산
        if mid < x:
            total += x - mid
    # 나무의 길이가 부족한 경우 더 많이 자르기 위해 왼쪽 탐색(mid 값이 작아짐)
    if total < M:
        end = mid - 1
    # 나무의 길이가 충분한 경우 덜 자르기 위해 오른쪽 탐색(mid 값이 커짐)
    else:
        result = mid # 최대한 덜 자를수 있는 경우가 정답이므로 이 부분에서 result 기록
        start = mid + 1

print(result)
