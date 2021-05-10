# https://www.acmicpc.net/problem/15667

N = int(input())
dl = [0, 3]
# DP 방식으로 모든 경우의 수를 리스트에 저장
for i in range(1, 100):
    dl.append(dl[i] + 2 * i + 2) # 3, 7, 13, 21, ...
print(dl.index(N))
