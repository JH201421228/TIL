import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N, K = map(int, input().split())
    score_list = list(map(int, input().split()))

    score_list.sort(reverse=True)

    ans = 0
    for idx in range(K):
        ans += score_list[idx]
    print(f'#{test+1} {ans}')