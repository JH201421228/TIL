Test_Case = int(input())

for i in range(Test_Case):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))
    max_val = 0
    min_val = sum(input_list[0:M])

    for j in range(N - M + 1):
        if sum(input_list[j:j+M]) > max_val:
            max_val = sum(input_list[j:j+M])

    for j in range(N - M + 1):
        if sum(input_list[j:j+M]) < min_val:
            min_val = sum(input_list[j:j+M])

    print(f'#{i + 1} {max_val - min_val}')