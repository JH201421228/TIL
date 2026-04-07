import sys
input = sys.stdin.readline


def inside(x, y, sx, sy, size):
    return sx <= x <= sx + size and sy <= y <= sy + size


def can_cover(points, size):
    # 가장 아래 y
    py = min(y for x, y in points)

    # sx 후보:
    # 포함 여부가 바뀌는 건 sx = x 또는 sx = x - size 일 때뿐
    candidates = set()
    for x, y in points:
        if py <= y <= py + size:
            candidates.add(x)
            candidates.add(x - size)

    for sx in candidates:
        remain = []

        for x, y in points:
            if not inside(x, y, sx, py, size):
                remain.append((x, y))

        if not remain:
            return True, (sx, py), (sx, py)

        min_x = min(x for x, y in remain)
        max_x = max(x for x, y in remain)
        min_y = min(y for x, y in remain)
        max_y = max(y for x, y in remain)

        if max_x - min_x <= size and max_y - min_y <= size:
            return True, (sx, py), (min_x, min_y)

    return False, None, None


def solve():
    n = int(input().strip())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    lo, hi = 0, 60000

    ans_size = 60000
    ans_sq1 = (0, 0)
    ans_sq2 = (0, 0)

    while lo <= hi:
        mid = (lo + hi) // 2
        ok, sq1, sq2 = can_cover(points, mid)

        if ok:
            ans_size = mid
            ans_sq1 = sq1
            ans_sq2 = sq2
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans_size)
    print(ans_sq1[0], ans_sq1[1])
    print(ans_sq2[0], ans_sq2[1])


if __name__ == "__main__":
    solve()