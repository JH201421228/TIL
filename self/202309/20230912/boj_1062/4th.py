import sys
sys.stdin = open('input.txt')


def teach_u(start, cnt):
    if cnt == K - 5:
        num = 0
        for inner_str in str_list:
            for small_str in inner_str:
                if not alpha_list[ord(small_str)-ord('a')]:
                   break
            else:
                num += 1
        global ans
        if ans < num:
            ans = num

        return

    for idx in range(start, length):
        if not alpha_list[ord(learn_list[idx])-ord('a')]:
            alpha_list[ord(learn_list[idx])-ord('a')] = 1
            teach_u(idx + 1, cnt + 1)
            alpha_list[ord(learn_list[idx])-ord('a')] = 0

N, K = map(int, input().split())
str_list = [list(input()[4:-4]) for _ in range(N)]
# print(str_list)
alpha_list = [0] * 26
innit_alpha = list('antic')
for char in innit_alpha:
    alpha_list[ord(char) - ord('a')] = 1
# print(alpha_list)
learn_list = []
for inner in str_list:
    learn_list.extend(inner)
learn_list = list(set(learn_list) - set(innit_alpha)) # 앞으로 배워야 할 리스트
# print(learn_list)
ans = 0
length = len(learn_list)
if K >= 5:
    teach_u(0, 0)
    print(ans)
elif K == 26:
    print(N)
else:
    print(0)