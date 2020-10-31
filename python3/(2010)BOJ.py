import sys
n = int(sys.stdin.readline()) # 멀티탭의 갯수
sum = 0
for i in range(n):
	d = int(sys.stdin.readline()) # 각 콘센트 구멍의 갯수
	sum += d # 모든 멀티탭의 구멍의 갯수
print(sum - n + 1) # 맨 마지막 멀티탭은 연결되지 않으므로 +1
