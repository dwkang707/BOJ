# https://www.acmicpc.net/problem/14914

a, b = map(int, input().split())
n = 1
while n <= a or n <= b:
    if a % n == 0 and b % n == 0:
        print(n, a // n, b // n)
    n += 1
