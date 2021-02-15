# https://www.acmicpc.net/problem/10815

N = int(input())
array = list(map(int, input().split()))
array.sort()

M = int(input())
x = list(map(int, input().split()))

for target in x:
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            print(1, end=' ')
            break
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if start > end:
        print(0, end=' ')
