def get_pos_nums(num):
    pos_nums = []
    while num != 0:
        pos_nums.append(num % 10)
        num = num // 10
    return pos_nums

print("Input N: ")
n = int(input())
print(get_pos_nums(n))
if(n<99):
    print("Incorrect input, please check your numbers (they may be more then 99)")
else:
    print(get_pos_nums(n))