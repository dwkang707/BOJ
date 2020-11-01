# https://www.acmicpc.net/problem/1463

n = int(input())
l = [0, 0] # 0번째가 아닌 첫번째부터 최소 계산수를 저장

# l[4] = (1) l[3] + 1 or (2) l[2] + 1 중 최솟값
# l[5] = l[4] + 1 -> 5는 2와 3 모두 나누어지지 않기 때문
# l[6] = (1) l[5] + 1, (2) l[3] + 1 or (3) l[2] + 1 중 최솟값
for i in range(2, n + 1):
    l.append(l[i - 1] + 1)
    if i % 2 == 0:
        if l[i] > l[i // 2]:
            l[i] = l[i // 2] + 1
    if i % 3 == 0:
        if l[i] > l[i // 3]:
            l[i] = l[i // 3] + 1
print(l[n])

# temp1 branch
# test1 branch
# test2 branch
