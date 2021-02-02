# https://www.acmicpc.net/problem/11051

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

N, K = map(int, input().split())
coefficeint = factorial(N) // (factorial(K) * factorial(N - K))
print(coefficeint % 10007)
