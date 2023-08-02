import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    N, K = map(int, input().split())
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in range(1, N+1):
        test_list.append(i)

    total_num = 0
    for x in range(1, 1 << 12):
        result_list = []
        for y in range(12):
            if x & (1 << y):
                result_list.append(test_list[y])

        if sum(result_list) == K and len(result_list) == N:
            total_num += 1

    print(f'#{test_case+1} {total_num}')
