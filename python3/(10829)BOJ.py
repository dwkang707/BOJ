# https://www.acmicpc.net/problem/10829

def binary(N):
    if N <= 1:
        return str(1)
    else:
        return binary(N // 2) + str(N % 2)

N = int(input())
print(binary(N))
