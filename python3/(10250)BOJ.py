# https://www.acmicpc.net/problem/10250

T = int(input())
for _ in range(T):
    count = 0
    s = ""
    H, W, N = map(int, input().split())
    for i in range(1, W + 1):
        for j in range(1, H + 1):
            count += 1
            if count == N:
                if i < 10:
                    s = str(j) + "0" + str(i)
                else:
                    s = str(j) + str(i)
                break
        if s != "":
            break
    print(s)                    
