# https://www.acmicpc.net/problem/2576

min_num = 0
odd_count = 0
odd_sum = 0
for i in range(7):
    val = int(input())
    if val % 2 == 1:
        odd_sum += val
        odd_count += 1
        if min_num == 0:
            min_num = val
        else:
            if val < min_num:
                min_num = val

if odd_count == 0:
    print(-1)
else:
    print(odd_sum)
    print(min_num)
