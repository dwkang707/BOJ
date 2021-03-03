# https://www.acmicpc.net/problem/2755

N = int(input())
score = 0.0
total_credits = 0
for i in range(N):
    S = input()
    if S[len(S)-2:] == 'A+':
        score += int(S[-4:-2].strip()) * 4.3
    elif S[len(S)-2:] == 'A0':
        score += int(S[-4:-2].strip()) * 4.0
    elif S[len(S)-2:] == 'A-':
        score += int(S[-4:-2].strip()) * 3.7
    elif S[len(S)-2:] == 'B+':
        score += int(S[-4:-2].strip()) * 3.3
    elif S[len(S)-2:] == 'B0':
        score += int(S[-4:-2].strip()) * 3.0
    elif S[len(S)-2:] == 'B-':
        score += int(S[-4:-2].strip()) * 2.7
    elif S[len(S)-2:] == 'C+':
        score += int(S[-4:-2].strip()) * 2.3
    elif S[len(S)-2:] == 'C0':
        score += int(S[-4:-2].strip()) * 2.0
    elif S[len(S)-2:] == 'C-':
        score += int(S[-4:-2].strip()) * 1.7
    elif S[len(S)-2:] == 'D+':
        score += int(S[-4:-2].strip()) * 1.3
    elif S[len(S)-2:] == 'D0':
        score += int(S[-4:-2].strip()) * 1.0
    elif S[len(S)-2:] == 'D-':
        score += int(S[-4:-2].strip()) * 0.7
    else:
        score += int(S[-4:-2].strip()) * 0.0
    total_credits += int(S[-4:-2].strip())
print('%.2f' % ((score / total_credits) + 0.000000000001))
