# https://www.acmicpc.net/problem/10177

def check_row(l, a_sum):
    b_sum = 0
    for i in range(1, len(l)):
        for j in range(len(l)):
            b_sum += l[i][j]
        if a_sum != b_sum:
            return False
        b_sum = 0
    return True

def check_col(l, a_sum):
    b_sum = 0
    for i in range(len(l)):
        for j in range(len(l)):
            b_sum += l[j][i]
        if a_sum != b_sum:
            return False
        b_sum = 0
    return True

def check_dig(l, a_sum):
    b_sum = 0
    for i in range(len(l)):
        b_sum += l[i][i]
    if a_sum != b_sum:
        return False
    else:
        b_sum = 0
        for i in range(len(l)):
            for j in range(len(l)):
                if i + j == len(l) - 1:
                    b_sum += l[i][j]
        if a_sum != b_sum:
            return False
        else:
            return True

n = int(input())
for _ in range(n):
    m = int(input())
    l = []
    a_sum = 0
    for i in range(m):
        sub = list(map(int, input().split()))
        l.append(sub)
        a_sum += l[0][i]
    result = check_row(l, a_sum)
    if result == True:
        result = check_col(l, a_sum)
        if result == True:
            result = check_dig(l, a_sum)
            if result == True:
                print("Magic square of size %d" % m)
            else:
                print("Not a magic square")
        else:
            print("Not a magic square")
    else:
        print("Not a magic square")
        
