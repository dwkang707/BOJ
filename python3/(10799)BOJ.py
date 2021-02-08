# https://www.acmicpc.net/problem/10799

def pipe(s):
    sum = 0
    stack = []
    for i in range(len(s)):
        # 여는 괄호는 스택에 추가
        if s[i] == '(':
            stack.append(i)
        # 닫는 괄호일 때 레이저인지 파이프 끝인지 판별
        else:
            stack.pop()
            # 레이저
            if s[i - 1] == '(':
                sum += len(stack)
            # 파이프
            else:
                sum += 1
    return sum

s = input()
print(pipe(s))
