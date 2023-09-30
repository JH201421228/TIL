import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta0 = [(0, 1), (1, 1)] #status 0 -> 0, 2
delta1 = [(1, 0), (1, 1)] #status 1 -> 1, 2
delta2 = [(0, 1), (1, 0), (1, 1)] #status 2 -> 0, 1, 3
delta = [delta0, delta1, delta2]

def holiday(x, y, status):

    if x == y == N-1:
        global ans
        ans += 1
        return

    for dx, dy in delta[status]:
        if x+dx < N and y+dy < N:
            if not dx:
                if not housing[x + dx][y + dy]:
                    holiday(x+dx, y+dy, 0)
            elif not dy:
                if not housing[x + dx][y + dy]:
                    holiday(x+dx, y+dy, 1)
            else:
                if not housing[x+dx][y+dy] and not housing[x][y+dy] and not housing[x+dx][y]:
                    holiday(x+dx, y+dy, 2)

N = int(input())
housing = [list(map(int, input().split())) for _ in range(N)]
ans = 0
holiday(0, 1, 0)
print(ans)