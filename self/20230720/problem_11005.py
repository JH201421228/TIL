
info_num = list(map(int, range(10, 36)))
info_alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0
B_list = []
ans_list = []

N, B = map(int, input().split())

while N >= B:
    B_list.append(N % B)
    N = N // B

B_list.append(N)
B_list.reverse()

for i in range(len(B_list)):
    if B_list[i] in info_num:
        ans_list.append(info_alph[B_list[i] - 10])

    else:
        ans_list.append(str(B_list[i]))

# # 시험용 출력
# print(B_list)
# print(ans_list)

for i in ans_list:
    print(i, end = '')
