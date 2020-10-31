# https://www.acmicpc.net/problem/2588
a = int(input())
b = int(input())
tmp = b
print(a * (b % 10))
b //= 10
print(a * (b % 10))
b //= 10
print(a * (b % 10))
print(a * tmp)
