# https://www.acmicpc.net/problem/10828

import sys

# input()으로 입력시 시간초과 발생하여 sys.stdin.readline() 사용
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    s = sys.stdin.readline()
    if 'push' in s:
        stack.append(int(s[5:]))
    elif 'pop' in s:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in s:
        print(len(stack))
    elif 'empty' in s:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in s:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
