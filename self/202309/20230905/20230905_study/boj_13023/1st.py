import sys
sys.stdin = open('input.txt')


def fxxk_friend(start):

    if check_friends[start] == 5: # start인덱스의 친구수가 5명이 되면,
        global ans # ans를 1로 변경
        ans = 1
        return

    if not check_friends[start]: # 해당 친구가 가진 값을 1로 변경
        check_friends[start] = 1

    for next_friend in friend_map[start]: # start인덱스의 친구와 연결된 친구 중,
        if not check_friends[next_friend]: # 아직 확인되지 않은 친구라면,
            check_friends[next_friend] = check_friends[start] + 1 # 친구 한명 추가
            fxxk_friend(next_friend) # 다음 친구에 대해 함수 호출
            check_friends[next_friend] = 0 # 돌아오면서 리스트 초기화


N, M = map(int, input().split()) # 사람의 수, 친구 관계의 수
friend_map = [[] for _ in range(N)] # 사람의 수 만큼 빈 리스트를 가진 리스트 생성
for _ in range(M): # 친구 관계를 연결
    p1, p2 = map(int, input().split())
    friend_map[p1].append(p2)
    friend_map[p2].append(p1)
# print(friend_map)
ans = 0

for i in range(N):
    check_friends = [0] * N # 확인된 친구인지 체크할 리스트 생성
    fxxk_friend(i, N) # i번째 친구에 대해 함수 호출
    if ans:
        print(ans)
        break
else:
    print(ans)