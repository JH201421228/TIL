import sys
from itertools import combinations
sys.stdin = open('input.txt')


def is_these_cities_linked_A():
    if len(AA) == 1:
        return True
    ans = 1
    stack = [AA[0]]
    check_list = [0] * N
    check_list[AA[0]] = 1

    while stack:
        now = stack.pop()
        for next in city_map[now]:
            if not check_list[next] and next not in BB:
                stack.append(next)
                check_list[next] = 1
                ans += 1
    if ans == len(AA):
        return True
    else:
        return False


def is_these_cities_linked_B():
    if len(BB) == 1:
        return True
    ans = 1
    stack = [BB[0]]
    check_list = [0] * N
    check_list[BB[0]] = 1

    while stack:
        now = stack.pop()
        for next in city_map[now]:
            if not check_list[next] and next not in AA:
                stack.append(next)
                check_list[next] = 1
                ans += 1
    if ans == len(BB):
        return True
    else:
        return False


N = int(input())
voter = list(map(int, input().split()))
city_map = [[] for _ in range(N)]
for i in range(N):
    info = list(map(int, input().split()))
    for idx in range(info[0]):
        city_map[i].append(info[idx+1] - 1)

A_cities = []
all_set = set(range(N))
for i in range(1, N//2 + 1):
    A_cities.extend(list(combinations(range(N), i)))

ans_list = []
for inner in A_cities:
    A_sum = 0
    B_sum = 0
    BB = list(all_set - set(inner))
    AA = list(inner)
    # print(AA, BB, is_these_cities_linked_A(), is_these_cities_linked_B())
    # print()
    if is_these_cities_linked_A() and is_these_cities_linked_B():
        for city in AA:
            A_sum += voter[city]
        for city in BB:
            B_sum += voter[city]
        ans_list.append(abs(A_sum - B_sum))

if ans_list:
    print(min(ans_list))
else:
    print(-1)
