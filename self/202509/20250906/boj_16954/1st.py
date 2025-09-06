import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 8방향 델타탐색
# 매번 도착 가능한 지점 을 맵에 찍임
# 벽을 한칸씩 내림 벽이 있던 부분은 .으로 바뀜
# 맵에 벽이 하나도 없을 때 맵에 남아있으면 도달 가능


delta = [(1, 1), (1, 0), (0, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]


def bfs():
    global G

    curs = []

    for i in range(8):
        for j in range(8):
            if G[i][j] == '*': curs.append((i, j))

    for i, j in curs:
        for di, dj in delta:
            ii, jj = i + di, j + dj

            if ii >= 0 and ii < 8 and jj >= 0 and jj < 8 and G[ii][jj] == '.':
                G[ii][jj] = '*'

    for j in range(8):
        if G[-1][j] == '#': G[-1][j] = '.'

    for i in range(7, 0, -1):
        for j in range(8):
            if G[i-1][j] == '#':
                G[i][j], G[i-1][j] = '#', '.'

    return


def isWall():
    global G

    for i in range(8):
        for j in range(8):
            if G[i][j] == '#': return True

    return False


def isCharacter():
    global G

    for i in range(8):
        for j in range(8):
            if G[i][j] == '*': return True

    return False


def main():
    global G
    G = [list(input().rstrip()) for _ in range(8)]
    G[-1][0] = '*'

    while True:
        curWallState = isWall()
        curCharacterState = isCharacter()

        if not curCharacterState:
            print(0)
            return

        if not curWallState:
            print(1)
            return

        bfs()

    return


if __name__ == "__main__":
    main()