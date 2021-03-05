# https://www.acmicpc.net/problem/11816

X = input()
result = 0
if X[0:2] == '0x':
    length = len(X[2:]) - 1
    hexa = X[2:]
    for i in range(len(hexa)):
        if hexa[i] == 'a':
            result += 10 * 16 ** length
        elif hexa[i] == 'b':
            result += 11 * 16 ** length
        elif hexa[i] == 'c':
            result += 12 * 16 ** length
        elif hexa[i] == 'd':
            result += 13 * 16 ** length
        elif hexa[i] == 'e':
            result += 14 * 16 ** length
        elif hexa[i] == 'f':
            result += 15 * 16 ** length
        else:
            result += int(hexa[i]) * 16 ** length
        length -= 1
else:
    if X[0] == '0':
        length = len(X[1:]) - 1
        octal = X[1:]
        for i in range(len(octal)):
            result += int(octal[i]) * 8 ** length
            length -= 1
    else:
        result = int(X)
print(result)
