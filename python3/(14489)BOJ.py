# https://www.acmicpc.net/problem/14489

A, B = map(int, input().split())
C = int(input())
balance = A + B
if balance >= 2 * C:
    print(balance - 2 * C)
else:
    print(balance)
