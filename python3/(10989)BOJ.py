# https://www.acmicpc.net/problem/10989

import sys
N = int(sys.stdin.readline().rstrip())
array = [0] * 10001
# 메모리 제한이 매우 낮은 문제여서 입력받은 모든 수를 list에 저장할 수 없다.
# 입력받은 수는 10000보다 작거나 같은 자연수 이므로 크기가 10001인 list를 만들고
# 입력받은 수마다 해당 인덱스에 있는 값을 1씩 증가시킴.
for i in range(N):
    a = int(sys.stdin.readline().rstrip())
    array[a] += 1

for i in range(1, 10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
