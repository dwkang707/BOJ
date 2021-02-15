# https://www.acmicpc.net/problem/2460

# max: 가장 많이 탑승했었던 인원 수, people: 현재 탑승 중인 인원 수
max = 0
people = 0
for i in range(10):
    # a: 하차 인원 수, b: 탑승 인원 수
    a, b = map(int, input().split())
    people += b - a
    if max < people:
        max = people
print(max)
