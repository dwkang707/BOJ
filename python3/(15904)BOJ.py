# https://www.acmicpc.net/problem/15904
s = input() # 문자열을 입력받음
UCPC = [0, 0, 0, 0]
for i in s:
    if i == "U" and UCPC[0] == 0:
        UCPC[0] += 1
    elif i == "C" and UCPC[0] != 0 and UCPC[3] == 0 and UCPC[1] == 0:
        UCPC[1] += 1
    elif i == "P" and UCPC[0] >= 1 and UCPC[1] >= 1:
        UCPC[2] += 1
    elif i == "C" and UCPC[0] >= 1 and UCPC[1] >= 1 and UCPC[2] >= 1:
        UCPC[3] += 1
    #print(UCPC[0], UCPC[1], UCPC[2], UCPC[3])
    if UCPC[0] >= 1 and UCPC[1] >= 1 and UCPC[2] >= 1 and UCPC[3] >= 1:
        print("I love UCPC")
        break
    
if UCPC[0] == 0 or UCPC[1] == 0 or UCPC[2] == 0 or UCPC[3] == 0:
    print("I hate UCPC")
