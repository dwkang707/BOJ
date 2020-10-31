l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum = 1

for _ in range(3):
	a = int(input())
	sum *= a

while True:
	r = sum % 10
	l[r] += 1
	sum //= 10
	if sum == 0:
		break

for i in range(10):
	print(l[i])