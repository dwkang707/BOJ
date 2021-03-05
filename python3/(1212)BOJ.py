# https://www.acmicpc.net/problem/1212

N = input()
for i in range(len(N)):
    if N[i] == '0':
        if i == 0:
            print('0', end='')
        else:
            print('000', end='')
    elif N[i] == '1':
        if i == 0:
            print('1', end='')
        else:
            print('001', end='')
    elif N[i] == '2':
        if i == 0:
            print('10', end='')
        else:
            print('010', end='')
    elif N[i] == '3':
        if i == 0:
            print('11', end='')
        else:
            print('011', end='')
    elif N[i] == '4':
        print('100', end='')
    elif N[i] == '5':
        print('101', end='')
    elif N[i] == '6':
        print('110', end='')
    elif N[i] == '7':
        print('111', end='')
