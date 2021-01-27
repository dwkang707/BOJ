# https://www.acmicpc.net/problem/2720

T = int(input())
for _ in range(T):
    q, d, n, p = 0, 0, 0, 0
    change = int(input())
    q = change // 25
    change = change % 25
    d = change // 10
    change = change % 10
    n = change // 5
    change = change % 5
    p = change
    print(q, d, n, p)
    
