# https://www.acmicpc.net/problem/5354

n = int(input())
for _ in range(n):
    val = int(input())
    for i in range(val):
        for j in range(val):
            if i == 0 or i == val - 1:
                print("#", end="")
            elif j == 0 or j == val - 1:
                print("#", end="")
            else:
                print("J", end="")
        print()
    print()
