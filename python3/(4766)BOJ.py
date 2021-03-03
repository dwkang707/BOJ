# https://www.acmicpc.net/problem/4766

c = 0
old = 0.0
while True:
    T = float(input())
    c += 1
    if int(T) == 999:
        break
    else:
        if c == 1:
            old = T
        else:
            print('%.2f' % (T - old))
            old = T
