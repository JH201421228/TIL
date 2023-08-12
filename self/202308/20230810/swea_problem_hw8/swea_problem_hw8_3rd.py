import sys
sys.stdin = open('input.txt')

def DFS():

    trace[0] = 1
    stack = [0]

    while stack:
        start = stack.pop()
        for next in range(100):
            if not trace[next] and can_go1[start] == next:
                trace[next] = 1
                stack.append(next)

                if next == 99:
                    return 1

            elif not trace[next] and can_go2[start] == next:
                trace[next] = 1
                stack.append(next)

                if next == 99:
                    return 1

    return 0

for _ in range(10):
    tc, E = map(int, input().split())
    map_list = list(map(int, input().split()))
    can_go1 = [0] * 100
    can_go2 = [0] * 100

    for i in range(E):
        if not can_go1[map_list[2*i]]:
            can_go1[map_list[2*i]] = map_list[2*i + 1]
        else:
            can_go2[map_list[2*i]] = map_list[2*i + 1]

    trace = [0] * 100
    print(f'#{tc} {DFS()}')