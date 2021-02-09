# https://www.acmicpc.net/problem/10845

import sys
from collections import deque

# input()으로 입력시 시간초과 발생하여 sys.stdin.readline() 사용
N = int(sys.stdin.readline())
queue = deque()
for i in range(N):
    s = sys.stdin.readline()
    if 'push' in s:
        queue.append(int(s[5:]))
    elif 'pop' in s:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif 'size' in s:
        print(len(queue))
    elif 'empty' in s:
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in s:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in s:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
