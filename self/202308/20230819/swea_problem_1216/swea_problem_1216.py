import sys
sys.stdin = open('input.txt')


def pal_checker():
    N = 100
    while N > 1:
        for i in range(100):
            for j in range(100 - N + 1):
                # print(j, j+N-1)
                check_list1 = hundred_list[i][j:j+N]
                check_list2 = trans_hundred_list[i][j:j+N]
                for k in range(N//2):
                    if check_list1[k] != check_list1[N-k-1]:
                        break
                else:
                    return N

                for k in range(N//2):
                    if check_list2[k] != check_list2[N-k-1]:
                        break
                else:
                    return N
        N -= 1
    return 1

for _ in range(10):
    N = int(input())
    hundred_list = [list(map(str, input())) for _ in range(100)]
    trans_hundred_list = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            trans_hundred_list[i][j] = hundred_list[j][i]
    print(f'#{N} {pal_checker()}')
