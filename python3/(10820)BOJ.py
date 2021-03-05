# https://www.acmicpc.net/problem/10820

while True:
    try:
        s = input()
        small, big, num, space = 0, 0, 0, 0
        for i in s:
            if 65 <= ord(i) <= 90:
                big += 1
            elif 97 <= ord(i) <= 122:
                small += 1
            elif 48 <= ord(i) <= 57:
                num += 1
            elif ord(i) == 32:
                space += 1
        print(small, big, num, space)
    except EOFError: # 몇 줄 까지 입력을 받아라 라는 말이 없기 때문에 EOFerror가 발생하면 종료시킴
        break
