# https://www.acmicpc.net/problem/13241

def gcd(a, b):
    # Make a largest
    if a < b:
        b, a = a, b
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b):
    div = gcd(a, b)
    result = (a * b) // div
    return result
    
A, B = map(int, input().split())
print(lcm(A, B))
