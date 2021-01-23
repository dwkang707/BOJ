t = int(input())
for _ in range(t):
	# n: 모든 닭의 다리수의 합, m: 닭의 수
	n, m = map(int, input().split())
	# t: 다리가 멀쩡한 닭의 수, u: 다리가 잘린 닭의 수
	t = u = 0
	tmp = m
	for _ in range(m):
		if tmp < n:
			n -= 2
			t += 1
			tmp -= 1
		else:
			n -= 1
			u += 1
			tmp -= 1
	print(u, t)
