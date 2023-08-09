import sys
sys.stdin = open('input.txt')


def pascal_s_tri(N):

    adding_list = [1]

    if N == 1:
        memo = [[1]]
        return memo
    else:
        memo = pascal_s_tri(N-1)
        inner_list = memo[-1]
        length = len(inner_list)
        for index in range(length - 1):
            adding_list.append(inner_list[index] + inner_list[index+1])
        adding_list.append(1)
        memo.append(adding_list)

        return memo


Test_Case = int(input())

for test_case in range(Test_Case):
    N = int(input())
    print(f'#{test_case + 1}')
    for inner_list in pascal_s_tri(N):
        print(*inner_list)