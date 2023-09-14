import sys
sys.stdin = open('input.txt')


def check_max_set():
    length = len(A_list)
    check_list = [1] * length

    for i in range(1, length):
        temp = []
        for j in range(i):
            if A_list[i] > A_list[j]:
                temp.append(check_list[j])
        if temp:
            check_list[i] = max(temp) + 1
    return max(check_list)

def check_min_set():
    length = len(B_list)
    check_list = [1] * length

    for i in range(1, length):
        temp = []
        for j in range(i):
            if B_list[i] < B_list[j]:
                temp.append(check_list[j])
        if temp:
            check_list[i] = max(temp) + 1
    return max(check_list)

N = int(input())
num_list = list(map(int, input().split()))
ans_list = []
# 리스트를 반으로 쪼개서 가장 큰 증가하는 수열과 가장 큰 감소하는 수열의 합을 구함
for point in range(N):
    A_list = num_list[:N-point]
    B_list = num_list[N-point-1:]
    # print(A_list, B_list)
    # print(check_max_set(), check_min_set())
    ans_list.append(check_max_set() + check_min_set())
print(max(ans_list) - 1)