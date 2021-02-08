# https://www.acmicpc.net/problem/10773

K = int(input())
stack = []
sum = 0
for i in range(K):
    n = int(input())
    if n != 0:
        stack.append(n)
        sum += n
    else:
        a = stack.pop() # list의 맨 오른쪽 원소 하나를 삭제 후 a에 저장
        sum -= a
print(sum)
