number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

total = 0

with open("input.txt", "r") as fp:
    for input_str in fp:

        digit1 = ""
        digit1_loc = 0
        for idx in range(len(input_str)):
            if input_str[idx].isdigit():
                digit1 = input_str[idx]
                digit1_loc = idx
                break

        for key in number_map.keys():
            sub_str_idx = input_str.find(key)
            if sub_str_idx != -1 and sub_str_idx < digit1_loc or digit1=="":
                digit1 = number_map[key]
                digit1_loc = sub_str_idx

        digit2 = ""
        digit2_loc = 0
        input_str2 = input_str[::-1]
        for idx in range(len(input_str)):
            if input_str2[idx].isdigit():
                digit2 = input_str2[idx]
                digit2_loc = len(input_str) - idx - 1
                break

        for key in number_map.keys():
            sub_str_idx = input_str.rfind(key)
            if sub_str_idx != -1 and sub_str_idx > digit2_loc or digit2=="":
                digit2 = number_map[key]
                digit2_loc = sub_str_idx

        number = int(digit1 + digit2)
        total += number

print(total)
