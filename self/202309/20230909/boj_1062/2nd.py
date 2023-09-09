import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']


def teach_u(start):
    if len(check_list) == K:
        check_num = 0
        for inner_str in str_list:
            for char in inner_str:
                if char not in check_list:
                    break
            else:
                check_num += 1
        global ans
        if ans < check_num:
            ans = check_num
        return

    for idx in range(start, length):
        check_list.append(alpha_list[idx])
        teach_u(start + 1)
        check_list.pop()


N, K = map(int, input().split())

check_list = ['a', 'n', 't', 'i', 'c']
str_list = []
for _ in range(N):
    input_str = input()
    input_str = input_str[4:]
    input_str = input_str[:-4]
    str_list.append(list(input_str))

alpha_set = set()
for inner in str_list:
    for char in inner:
        if char not in check_list:
            alpha_set.add(char)

alpha_list = list(alpha_set)
# print(alpha_set)
# print(alpha_list)
length = len(alpha_list)
# print(alpha_list)
# print(length)
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    ans = 0
    teach_u(0)
    print(ans)