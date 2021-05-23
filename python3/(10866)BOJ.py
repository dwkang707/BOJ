# https://www.acmicpc.net/problem/10866

from collections import deque
import sys

dq = deque()
n = int(input())
for i in range(n):
    command = sys.stdin.readline().strip()
    if 'push_front' in command:
        val = int(command[10:])
        dq.appendleft(val)
    elif 'push_back' in command:
        val = int(command[9:])
        dq.append(val)
    elif 'pop_front' in command:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif 'pop_back' in command:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif 'size' in command:
        print(len(dq))
    elif 'empty' in command:
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif 'back' in command:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
