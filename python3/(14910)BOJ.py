# https://www.acmicpc.net/problem/14910

array = list(map(int, input().split()))
if len(array) == 1:
    print('Good')
else:
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            print('Bad')
            break
        elif i == len(array) - 2 and array[i] <= array[i + 1]:
            print('Good')
