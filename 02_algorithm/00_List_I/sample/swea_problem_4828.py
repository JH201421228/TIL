Test_Case = int(input())

for i in range(Test_Case):
    numbers = int(input())
    numbers_list = list(map(int, input().split()))

    max_num = numbers_list[0]
    min_num = numbers_list[0]

    for number in numbers_list:
        if number > max_num:
            max_num = number

    for number in numbers_list:
        if number < min_num:
            min_num = number

    print(f'#{i + 1} {max_num - min_num}')