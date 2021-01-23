N = int(input())
b = N
w = 0
for i in range(N):
	if (i + 1) % 2 == 0:
		b = b + (N // (i + 1))
		w = w + (N // (i + 1))
	else:
		b = b - (N // (i + 1))
		w = w + (N // (i + 1))
print(w)