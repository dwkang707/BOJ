# https://www.acmicpc.net/problem/10156

# 과자 한 개의 가격 K, 사려고 하는 과자의 개수 N, 현재 동수가 가진 돈 M
K, N, M = map(int, input().split())
if K * N > M:
    print(K * N - M)
else:
    print(0)
    
