Test_Case = 10

for i in range(Test_Case):

    dump_num = int(input())
    box_list = list(map(int, input().split()))

    for j in range(dump_num):
        max_val = max(box_list)
        min_val = min(box_list)
        max_index = box_list.index(max_val)
        min_index = box_list.index(min_val)

        box_list[max_index] -= 1
        box_list[min_index] += 1

    print(f'#{i + 1} {max(box_list) - min(box_list)}')