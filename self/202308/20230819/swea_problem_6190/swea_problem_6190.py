import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = []
    for i in range(N-1):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]
            num_list = list(map(int, str(num)))
            num_len = len(num_list)
            for k in range(num_len - 1):
                if num_list[k] > num_list[k + 1]:
                    break
            else:
                ans.append(num)

    if ans:
        print(f'#{test + 1} {max(ans)}')
    else:
        print(f'#{test + 1} -1')