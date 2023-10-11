import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def leviating():
    que = deque([(0, 0, C)])
    visited = [[[0] * (C+1) for _ in range(B+1)] for _ in range(A+1)]
    visited[0][0][C] = 1
    ans_set = set()
    ans_set.add(C)
    while que:
        a, b, c = que.popleft()
        if a + b:
            mix_ab = a+b

            if mix_ab <= A and not visited[mix_ab][0][c]:
                visited[mix_ab][0][c] = 1
                que.append((mix_ab, 0, c))

            elif mix_ab > A and not visited[A][mix_ab-A][c]:
                visited[A][mix_ab - A][c] = 1
                que.append((A, mix_ab-A, c))



            if mix_ab <= B and not visited[0][mix_ab][c]:
                visited[0][mix_ab][c] = 1
                que.append((0, mix_ab, c))
                ans_set.add(c)

            elif mix_ab > B and not visited[mix_ab-B][B][c]:
                visited[mix_ab-B][B][c] = 1
                que.append((mix_ab-B, B, c))

        if a + c:
            mix_ac = a + c

            if mix_ac <= A and not visited[mix_ac][b][0]:
                visited[mix_ac][b][0] = 1
                que.append((mix_ac, b, 0))

            elif mix_ac > A and not visited[A][b][mix_ac-A]:
                visited[A][b][mix_ac-A] = 1
                que.append((A, b, mix_ac-A))

            if mix_ac <= C and not visited[0][b][mix_ac]:
                visited[0][b][mix_ac] = 1
                que.append((0, b, mix_ac))
                ans_set.add(mix_ac)

            elif mix_ac > C and not visited[mix_ac - C][b][C]:
                visited[mix_ac - C][b][C] = 1
                que.append((mix_ac - C, b, C))

        if b + c:
            mix_bc = b + c

            if mix_bc <= B and not visited[a][mix_bc][0]:
                visited[a][mix_bc][0] = 1
                que.append((a, mix_bc, 0))


            elif mix_bc > B and not visited[a][B][mix_bc - B]:
                visited[a][B][mix_bc - B] = 1
                que.append((a, B, mix_bc - B))
                if not a:
                    ans_set.add(mix_bc - B)

            if mix_bc <= C and not visited[a][0][mix_bc]:
                visited[a][0][mix_bc] = 1
                que.append((a, 0, mix_bc))
                if not a:
                    ans_set.add(mix_bc)

            elif mix_bc > C and not visited[a][mix_bc-C][C]:
                visited[a][mix_bc-C][C] = 1
                que.append((a, mix_bc-C, C))
                if not a:
                    ans_set.add(C)

    return sorted(list(ans_set))

# A, B, C는 병의 상태
# 처음에는 C만 가득 차 있음
# A, B, C 각각 0으로 가득찬 리스트를 만들어서 비우고 채우는 과정을 탐색
A, B, C = map(int, input().split())

visited = leviating()
print(*visited)

