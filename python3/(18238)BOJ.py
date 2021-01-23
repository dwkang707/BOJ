input_data = input()
location = int(ord('A'))
time = 0

# ord 내장 함수는 ASCII code를 반환하는 함수
# abs(int(ord(i)) - location)는 시계방향
# abs(26 - abs(int(ord(i)) - location))는 반시계방향
for i in input_data:
    if abs(int(ord(i)) - location) < abs(26 - abs(int(ord(i)) - location)):
        time += abs(int(ord(i)) - location)
    else:
        time += abs(26 - abs(int(ord(i)) - location))
    location = int(ord(i))
    
print(time)
