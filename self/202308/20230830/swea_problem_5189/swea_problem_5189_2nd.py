import sys
sys.stdin = open('input.txt')


def charge_func():
    total = charge_list[ans_list[-1]][ans_list[0]]
    for i in range(len(ans_list)-1):
        total += charge_list[ans_list[i]][ans_list[i + 1]]
    return total



def why_do_golf(N):
    if len(ans_list) == N:
        print(charge_func())
        return

    for cordinate in range(N):
        if cordinate not in ans_list:
            ans_list.append(cordinate)
            why_do_golf(N)
            ans_list.pop()


T = int(input())
for test in range(T):
    N = int(input())
    charge_list = [list(map(int, input().split())) for _ in range(N)]
    print(charge_list)
    ans_list = []
    why_do_golf(N)
    print('-------------')