# https://www.acmicpc.net/problem/10822

S = list(map(int, input().split(",")))
sum = 0
for i in range(len(S)):
    sum += S[i]
print(sum)
