# https://www.acmicpc.net/problem/1065
def hansu(n):
    if n < 100:
        print(n)
    else:
        count = 99
        for i in range(100, n + 1):
            # a: 100의 자리, b: 10의 자리, c: 1의 자리
            a = i // 100
            b = (i % 100) // 10
            c = i % 10
            if a - b == b - c:
                count += 1
        print(count)

n = int(input())
hansu(n)
