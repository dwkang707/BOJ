# https://www.acmicpc.net/problem/10872
def fac(n):
	if n < 1:
		return 1
	else:
		return n * fac(n - 1)

i = int(input())
print(fac(i))
