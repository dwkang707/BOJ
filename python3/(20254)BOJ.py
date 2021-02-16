# https://www.acmicpc.net/problem/20254

# UR, TR, UO, and TO.
UR, TR, UO, TO = map(int, input().split())
# 56UR + 24TR + 14UO + 6TO
result = 56 * UR + 24 * TR + 14 * UO + 6 * TO
print(result)
