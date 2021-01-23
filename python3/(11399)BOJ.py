# https://www.acmicpc.net/problem/11399
n = int(input())
l = list(map(int, input().split()))
l.sort()
time = 0 # 각 이용자가 ATM 기기를 이용하여 돈을 인출하는데 걸리는 시간
sum = 0 # ATM 기기 사용시간 총 합

for i in l:
    time += i
    sum += time
print(sum)
