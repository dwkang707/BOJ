# https://www.acmicpc.net/problem/17945

import math
A, B = map(int, input().split())
x1 = - A - int(math.sqrt(math.pow(A, 2) - B))
x2 = - A + int(math.sqrt(math.pow(A, 2) - B))
if x1 == x2:
    print(x1)
else:
    print(x1, x2)
