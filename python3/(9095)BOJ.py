# https://www.acmicpc.net/problem/9095

n = int(input())

for _ in range(n):
    # T(1) = 1, T(2) = 2, T(3) = 4, T(4)=T(3)+T(2)+T(1), ... , T(n)=T(n-3)+T(n-2)+T(n-1) where n > 3
    l = [0, 1, 2, 4]
    value = int(input())
    if value <= 3:
        print(l[value])
    else:
        for i in range(4, value + 1):
            l.append(l[i - 3] + l[i - 2] + l[i - 1])
        print(l[value])
