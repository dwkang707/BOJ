# https://www.acmicpc.net/problem/4892
i = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    else:
        n1 = 3 * n0
        if n1 % 2 == 0:
            n2 = n1 // 2
            n3 = 3 * n2
            n4 = n3 // 9
            print(str(i) + ". even", n4)
        else:
            n2 = (n1 + 1) // 2
            n3 = 3 * n2
            n4 = n3 // 9
            print(str(i) + ". odd", n4)
        i += 1
