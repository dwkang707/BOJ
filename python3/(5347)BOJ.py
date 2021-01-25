# https://www.acmicpc.net/problem/5347

def gcd(a, b): # 최대공약수(유클리드 알고리즘)
    # make a largest
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b): # 최소공배수
    result = (a * b) // gcd(a, b)
    return result

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))
