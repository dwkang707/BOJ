# https://www.acmicpc.net/problem/10870
def fibonacci(n):
    if n <= 1:
        return n
    else:
        l = [0, 1]
        for i in range(n):
            l.append(l[i] + l[i + 1])
        return l[n]

n = int(input())
result = fibonacci(n)
print(result)
