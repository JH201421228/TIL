import sys
from itertools import combinations
sys.stdin = open('input.txt')


def is_these_cities_linked_A():
    if len(AA) == 1: # 도시가 1개이면 연결 여부를 조사할 필요 없다.
        return True
    ans = 1
    stack = [AA[0]]
    check_list = [0] * N
    check_list[AA[0]] = 1

    while stack:
        now = stack.pop()
        for next in city_map[now]: # 현재 도시에서 갈 수 있는 도시중에
            if not check_list[next] and next not in BB: # 아직 방문하지 않았고, 다른 군집에 엮여있지 않다면
                stack.append(next)
                check_list[next] = 1
                ans += 1
    if ans == len(AA): # 해당 조건이면 군집 내의 모든 도시를 순회할 수 있음을 의미함
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
city_map = [[] for _ in range(N)] # 도시간의 연결 정보를 나타내는 배열
for i in range(N):
    info = list(map(int, input().split()))
    for idx in range(info[0]):
        city_map[i].append(info[idx+1] - 1)

A_cities = []
all_set = set(range(N))
for i in range(1, N//2 + 1): # 전체 도시 수의 절반까지만 생각(나머지는 B에 묶을 예정)
    A_cities.extend(list(combinations(range(N), i))) # A로 엮일 수 있는 모든 경우의 수
print(A_cities)
print(all_set)
ans_list = []
for inner in A_cities: # A 도시 군 후보 리스트를 순회하면서
    A_sum = 0
    B_sum = 0
    BB = list(all_set - set(inner)) # B 도시군 후보는 전체에서 A 도시군 후보를 뺀 나머지
    AA = list(inner)

    if is_these_cities_linked_A() and is_these_cities_linked_B(): # A 도시군과 B 도시군이 서로 연결 되어 있는지 확인
        for city in AA:
            A_sum += voter[city] # A 군집의 모든 투표권 합
        for city in BB:
            B_sum += voter[city] # B 군집의 모든 투표권 합
        ans_list.append(abs(A_sum - B_sum)) # 차이를 리스트에 추가

if ans_list: # 결과 출력
    print(min(ans_list))
else:
    print(-1)
