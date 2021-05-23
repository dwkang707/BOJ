# https://www.acmicpc.net/problem/2562

num_list = []
for i in range(9):
    num_list.append(int(input()))
sorted_list = sorted(num_list)
print(sorted_list[8])
print(num_list.index(sorted_list[8]) + 1)
