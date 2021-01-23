order = 1
while True:
    print_str = ""
    input_str = input()
    if input_str == "Was it a cat I saw?":
        break
    else:
        print_str += input_str[0]
        # 0, 2, 4, 8, ...
        # 0, 3, 6, 9, ...
        # 0, 4, 8, 12, ... 와 같은 순서임
        order += 1
        for i in range(1, len(input_str)):
            if i % order == 0:
                print_str += input_str[i]
        print(print_str)
