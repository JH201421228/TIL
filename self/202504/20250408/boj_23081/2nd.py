import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 8방향
DIRECTIONS = [(-1, -1), (0, -1), (1, -1),
              (-1, 0),          (1, 0),
              (-1, 1),  (0, 1),  (1, 1)]

def inside(x, y, N):
    return 0 <= x < N and 0 <= y < N

def count_flips(board, x, y, N):
    total_flips = 0

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        flips = 0
        while inside(nx, ny, N) and board[ny][nx] == 'W':
            flips += 1
            nx += dx
            ny += dy
        if inside(nx, ny, N) and board[ny][nx] == 'B':
            total_flips += flips
        else:
            continue

    return total_flips

def find_best_move(board, N):
    max_flips = 0
    best_move = None

    for y in range(N):
        for x in range(N):
            if board[y][x] != '.':
                continue
            flips = count_flips(board, x, y, N)
            if flips > 0:
                if flips > max_flips:
                    max_flips = flips
                    best_move = (x, y)
                elif flips == max_flips:
                    if y < best_move[1] or (y == best_move[1] and x < best_move[0]):
                        best_move = (x, y)

    return best_move, max_flips

def main():
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    move, flips = find_best_move(board, N)
    if move is None:
        print("PASS")
    else:
        print(f"{move[0]} {move[1]}")
        print(flips)

if __name__ == "__main__":
    main()
