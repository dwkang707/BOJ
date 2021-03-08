# https://www.acmicpc.net/problem/1373

binary = input()
octal = ""
length = len(binary)
i = 0
if length % 3 == 2:
    binary = "0" + binary
    length += 1
elif length % 3 == 1:
    binary = "00" + binary
    length += 2
while length != i:
    if binary[i:i + 3] == "001":
        octal += "1"
    elif binary[i:i + 3] == "010":
        octal += "2"
    elif binary[i:i + 3] == "011":
        octal += "3"
    elif binary[i:i + 3] == "100":
        octal += "4"
    elif binary[i:i + 3] == "101":
        octal += "5"
    elif binary[i:i + 3] == "110":
        octal += "6"
    elif binary[i:i + 3] == "111":
        octal += "7"
    elif binary[i:i + 3] == "000":
        octal += "0"
    i += 3
print(octal)
