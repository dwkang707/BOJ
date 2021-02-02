# https://www.acmicpc.net/problem/1850

def gcd(a, b):
    # Make a largest
    if a < b:
        b, a = a, b
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a

A, B = map(int, input().split())
div = gcd(A, B)
s = ""
for _ in range(div):
    s += "1"
print(s)
