import sys
sys.stdin = open('input.txt')

# ############절취선#################

Test_Case = int(input())

for test_case in range(Test_Case):
    N = int(input())
    score_list = list(map(int, input().split()))
    total_score = 0
    # 값을 입력받는 부분.

    for plus_num in range(1, N + 1):
        index = 0
        while index < N:
            total_score += score_list[index]
            index += plus_num
    # 1번 건너뛰기 부터 N번 건너뛰기 까지 수행하면서 각 값을 total_score에 더함.

    if total_score > 0:
        print(f'#{test_case + 1} {total_score}')
    else:
        print(f'#{test_case + 1} 0')
    # total_score 의 값에 따라 원하는 값을 출력.