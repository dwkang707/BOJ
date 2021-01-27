# https://www.acmicpc.net/problem/10181

def perfect_num(n):
    l = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
            sum += i

    if n == sum:
        print("%d = " % n, end="")
        for i in range(len(l)):
            if i < len(l) - 1:
                print("%d + " % l[i], end="")
            else:
                print("%d" % l[i])
    else:
        print("%d is NOT perfect." % n)

while True:
    n = int(input())
    if n == -1:
        break
    else:
        perfect_num(n)
