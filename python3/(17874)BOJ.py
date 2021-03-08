# https://www.acmicpc.net/problem/17874

n, h, v = map(int, input().split())
vol = 4
half = n / 2
if h >= half and v >= half:
    vol *= h * v
elif h >= half and v < half:
    vol *= h * (n - v)
elif h < half and v >= half:
    vol *= (n - h) * v
else:
    vol *= (n - h) * (n - v)
print(vol)
