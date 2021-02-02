# https://www.acmicpc.net/problem/3036

def gcd(a, b):
    # Make a largest
    if a < b:
        b, a = a, b
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a
    
N = int(input())
radius = list(map(int, input().split()))
for i in range(1, N):
    div = gcd(radius[0], radius[i])
    print(radius[0] // div, "/", radius[i] // div, sep="")
