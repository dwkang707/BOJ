days, today = map(int, input().split())
A, B, C, D = map(float, input().split())
gd = (A + C) * 1000 / days
sd = (B + D) * 1000 / days
print(int(gd))
print(int(sd))