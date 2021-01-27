# https://www.acmicpc.net/problem/1712
# https://ko.wikipedia.org/wiki/%EC%86%90%EC%9D%B5%EB%B6%84%EA%B8%B0%EC%A0%90

A, B, C = map(int, input().split())
if B >= C:
    print(-1)
else:
    x = A // (C - B)
    print(x + 1)
