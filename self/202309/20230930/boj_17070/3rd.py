import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# delta0 = [(0, 1), (1, 1)] #status 0 -> 0, 2
# delta1 = [(1, 0), (1, 1)] #status 1 -> 1, 2
# delta2 = [(0, 1), (1, 0), (1, 1)] #status 2 -> 0, 1, 3
# delta = [delta0, delta1, delta2]

def holiday(x, y, status):

    if x == y == N-1:
        global ans
        ans += 1
        return


    if x+1 < N and y+1 < N:
        if not housing[x+1][y+1] and not housing[x+1][y] and not housing[x][y+1]:
             holiday(x+1, y+1, 2)
    if status != 1 and y+1 < N:
        if not housing[x][y + 1]:
            holiday(x, y+1, 0)
    if status and x + 1 < N:
        if not housing[x+1][y]:
            holiday(x+1, y, 1)

N = int(input())
housing = [list(map(int, input().split())) for _ in range(N)]
ans = 0
holiday(0, 1, 0)
print(ans)