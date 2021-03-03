# https://www.acmicpc.net/problem/5218

T = int(input())
for i in range(T):
    A, B = input().split()
    print("Distances:", end=' ')
    for j in range(len(A)):
        if A[j] <= B[j]:
            print(ord(B[j]) - ord(A[j]), end=' ')
        else:
            print((ord(B[j]) + 26) - ord(A[j]), end=' ')
    print()
