# https://www.acmicpc.net/problem/16395
import math
def binomial_coefficient(n, k):
    result = 0
    if n - 1 < 1 or k - 1 < 1:
        result = 1
    else:
        result = (math.factorial(n - 1)) // (math.factorial(k - 1) * math.factorial(n - k))
    return result

n, k = map(int, input().split())
result = binomial_coefficient(n, k)
print(result)
