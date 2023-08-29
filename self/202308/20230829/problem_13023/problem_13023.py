import sys
sys.stdin = open('input.txt')


def why_do_this(N):
    stack = [0]
    friendship = [0] * N
    friendship[0] = 1
    return_list = [0]
    while stack:
        friend = stack.pop()
        for next_friend in range(N):
            if friend_map[friend][next_friend]:
                return_list.append()

N, M = map(int, input().split())
friend_map = [[0] * N for _ in range(N)]
for _ in range(M):
    p1, p2 = map(int, input().split())
    friend_map[p1][p2] = 1
    friend_map[p2][p1] = 1
print(friend_map)
