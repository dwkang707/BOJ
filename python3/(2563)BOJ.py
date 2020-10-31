# https://www.acmicpc.net/problem/2563
paper = []

# 100행을 만든다.
for _ in range(100):
	paper.append([])

# 100열을 만들고 각 원소를 0으로 채운다.
for i in range(100):
	for _ in range(100):
		paper[i].append(0)

n = int(input())
for _ in range(n):
	a, b = map(int, input().split())
	
	# 색종이가 덮어지는 부분의 좌표만 1로 채운다.
	for i in range(a, a + 10):
		for j in range(b, b + 10):
			paper[i][j] = 1

result = 0
for i in range(100):
	for j in range(100):
		result += paper[i][j]
print(result)