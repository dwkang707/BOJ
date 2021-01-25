# https://www.acmicpc.net/problem/10178

n = int(input())
for _ in range(n):
    c, v = map(int, input().split())
    bro = c // v
    dad = c % v
    print("You get %d piece(s) and your dad gets %d piece(s)." % (bro, dad))
