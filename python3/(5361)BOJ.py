# https://www.acmicpc.net/problem/5361

rifle = 350.34
visual_sensor = 230.90
ear_sensor = 190.55
arm = 125.30
leg = 180.90
n = int(input())

for _ in range(n):
    A, B, C, D, E = map(int, input().split())
    sum = rifle * A + visual_sensor * B + ear_sensor * C + arm * D + leg * E
    print("$%.2f" % round(sum, 2))
