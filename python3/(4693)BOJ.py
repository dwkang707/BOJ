# https://www.acmicpc.net/problem/4693

# 10_001에서 _은 자릿수를 구분하기 위해 사용(일반 숫자에서 ,로 구분하는것과 동일한 의미) -> 숫자 리터럴로 인식
numbers = list(range(1, 10_001))
r_list = []  # 이후에 삭제할 숫자 list
for i in numbers:
    for j in str(num):
        i += int(j)  # 생성자가 있는 숫자
    if i <= 10_000:
        remove_list.append(i)

for r_num in set(r_list) :  # set으로 중복값 제거(set은 집합이므로 중복값을 하나로 합쳐줌)
    numbers.remove(r_num)
for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 list
    print(self_num)
