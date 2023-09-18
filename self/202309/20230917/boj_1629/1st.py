import sys
sys.stdin = open('input.txt')


A, B, C = map(int, input().split())

test_num = 1
ans_list = []
while True:
    test_num = (test_num * A) % C
    if test_num not in ans_list:
        ans_list.append(test_num)
    else:
        break
# print(ans_list)
print(ans_list[B % len(ans_list)])