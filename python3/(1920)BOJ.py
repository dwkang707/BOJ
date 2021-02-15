# https://www.acmicpc.net/problem/1920

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None

N = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, N - 1)
    if result != None:
        print(1)
    else:
        print(0)
