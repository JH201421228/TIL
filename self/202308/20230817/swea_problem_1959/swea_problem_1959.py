import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    ans_list = []
    if N > M:
        for i in range(N - M + 1):
            ans = 0
            for j in range(M):
                ans += M_list[j]*N_list[i+j]
            ans_list.append(ans)
    elif M > N:
        for i in range(M - N + 1):
            ans = 0
            for j in range(N):
                ans += N_list[j]*M_list[i+j]
            ans_list.append(ans)
    else:
        ans = 0
        for i in range(N):
            ans += N_list[i]*M_list[i]
        ans_list.append(ans)

    print(f'#{test+1} {max(ans_list)}')