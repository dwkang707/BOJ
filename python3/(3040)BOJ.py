# https://www.acmicpc.net/problem/3040

# l: 9개의 입력받을 정수를 저장, sum: 입력받은 9개의 정수의 합, index1, 2: 난쟁이가 아닌 번호 2개
l = []
sum = 0
index1, index2 = 0, 0

# 9개의 정수를 입력 받음
for i in range(9):
    l.append(int(input()))
    sum += l[i]

# 7명의 난쟁이의 번호의 합이 100, 난쟁이에 포함되지 않은 2명의 번호의 합: sum - 100
d = sum - 100

# 순차비교하면서 d의 값이 되는 2개의 인덱스를 찾는다.
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] < d:
            index1 = i
            
            if l[index1] + l[j] == d:
                index2 = j
                break
        else:
            break
    if index2 != 0:
        break

for i in range(len(l)):
    if i != index1 and i != index2:
        print(l[i])
