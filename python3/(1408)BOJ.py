# https://www.acmicpc.net/problem/1408

a1, a2, a3 = map(int, input().split(':'))
b1, b2, b3 = map(int, input().split(':'))
time = 0
while a1 != b1 or a2 != b2 or a3 != b3:
    a3 += 1
    time += 1 # 입력한 두 시간이 같아질 때까지 1초씩 올림
    if a3 == 60:
        a3 = 0
        a2 += 1
        if a2 == 60:
            a2 = 0
            a1 += 1
            if a1 == 24:
                a1 = 0
s = time % 60
m = (time // 60) % 60
h = (time // 60) // 60
print(f'{h:0>2}:{m:0>2}:{s:0>2}')
