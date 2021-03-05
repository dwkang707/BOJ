# https://www.acmicpc.net/problem/14915

# 진법 변환 tail-recursion 구현
def digit_convert(m, n, result = ""):
    if m == 0:
        return result
    else:
        if m % n >= 10:
            if m % n == 10:
                result = "A" + result
            elif m % n == 11:
                result = "B" + result
            elif m % n == 12:
                result = "C" + result
            elif m % n == 13:
                result = "D" + result
            elif m % n == 14:
                result = "E" + result
            else:
                result = "F" + result
        else:
            result = str(m % n) + result
        return digit_convert(m // n, n, result)

m, n = map(int, input().split())
if m == 0:
    print(0)
else:
    print(digit_convert(m, n))
