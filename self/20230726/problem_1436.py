N = int(input())
count_num = 0
ans_num = '666'

while True:
    if '666' in ans_num:
        count_num += 1

    if count_num == N:
        break

    ans_num = str(int(ans_num)+1)

print(int(ans_num))