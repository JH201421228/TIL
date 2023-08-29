import sys
sys.stdin = open('input.txt')


def fxxk_friend(start, N):

    if check_friends[start] == 5:
        global ans
        ans = 1
        return

    if not check_friends[start]:
        check_friends[start] = 1

    for next_friend in friend_map[start]:
        if not check_friends[next_friend]:
            check_friends[next_friend] = check_friends[start] + 1
            fxxk_friend(next_friend, N)
            check_friends[next_friend] = 0


N, M = map(int, input().split())
friend_map = [[] for _ in range(N)]
for _ in range(M):
    p1, p2 = map(int, input().split())
    friend_map[p1].append(p2)
    friend_map[p2].append(p1)
# print(friend_map)
ans = 0

for i in range(N):
    check_friends = [0] * N
    fxxk_friend(i, N)
    if ans:
        print(ans)
        break
else:
    print(ans)