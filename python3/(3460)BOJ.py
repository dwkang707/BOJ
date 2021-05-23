# https://www.acmicpc.net/problem/3460

n = int(input())
for i in range(n):
    binary = int(input())
    binary_list = [] # 10진수를 2진수로 계산하여 저장할 리스트
    while binary != 0:
        binary_residue = binary % 2
        binary_list.append(binary_residue) # 2로 나눈 나머지를 리스트에 저장
        binary //= 2
    for j in range(len(binary_list)):
        if binary_list[j] == 1:
            print(j, end=' ')
