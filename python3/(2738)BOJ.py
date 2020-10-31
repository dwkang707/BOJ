# https://www.acmicpc.net/problem/2738
row, col = map(int, input().split())
A = []
for i in range(row):
	line = []
	for j in range(col):
		a = int(input())
		line.append(a)
	A.append(line)
print(A)
