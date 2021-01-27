# https://www.acmicpc.net/problem/2475

l = list(map(int, input().split()))
sum = 0
for i in range(len(l)):
    sum += l[i] * l[i]
val = sum % 10
print(val)
