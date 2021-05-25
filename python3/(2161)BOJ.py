# https://www.acmicpc.net/problem/2161

from collections import deque
n = int(input())
card = deque()
discard_card = []
for i in range(1, n + 1):
    card.append(i)
while 1 < len(card):
    discard_card.append(card.popleft()) # 맨 앞의 카드를 제거한 후 제거한 카드 목록에 추가
    n = card.popleft() # 맨 앞의 카드를 맨 뒤에 넣기 위해 변수에 저장
    card.append(n) # 변수에 저장한 맨 앞의 카드 정보를 맨 뒤에 추가
discard_card.append(card.popleft()) # 마지막 남은 카드 한 장을 제거한 카드 목록에 추가
for i in discard_card:
    print(i, end=' ')
