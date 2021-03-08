# https://www.acmicpc.net/problem/19944

N, M = map(int, input().split())
if 1 <= M <= 2:
    print("NEWBIE!")
elif 2 < M <= N:
    print("OLDBIE!")
else:
    print("TLE!")
