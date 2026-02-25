import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

DAY = 24 * 60 * 60  # 86400


def to_sec(s: str) -> int:
    h, m, sec = map(int, s.split(":"))
    return h * 3600 + m * 60 + sec


def parse_interval(line: str):
    a, b = line.strip().split(" - ")
    return to_sec(a), to_sec(b)


def add_interval(diff, l, r):
    """inclusive [l, r]"""
    diff[l] += 1
    diff[r + 1] -= 1


def add_cyclic_interval(diff, s, e):
    """24시간 원형 구간 inclusive [s..e]"""
    if s <= e:
        add_interval(diff, s, e)
    else:
        # 자정 넘김 -> 두 구간으로 분할
        add_interval(diff, s, DAY - 1)
        add_interval(diff, 0, e)


def range_sum(ps, l, r):
    """inclusive [l, r] 합, ps는 길이 DAY+1 prefix"""
    return ps[r + 1] - ps[l]


def cyclic_sum(ps, s, e):
    """원형 구간 [s..e]의 합 (inclusive)"""
    if s <= e:
        return range_sum(ps, s, e)
    else:
        return range_sum(ps, s, DAY - 1) + range_sum(ps, 0, e)


def cyclic_len(s, e):
    """원형 구간 길이 (inclusive 초 개수)"""
    if s <= e:
        return e - s + 1
    else:
        return (DAY - s) + (e + 1)


def solve():
    N = int(input())

    # diff는 r+1 접근 위해 DAY+1 인덱스 필요 => 길이 DAY+1
    # 안전하게 +2
    diff = [0] * (DAY + 2)

    for _ in range(N):
        s, e = parse_interval(input())
        add_cyclic_interval(diff, s, e)

    # 차분 -> 초별 인기도
    watchers = [0] * DAY
    cur = 0
    for t in range(DAY):
        cur += diff[t]
        watchers[t] = cur

    # 누적합 ps[i] = watchers[0..i-1] 합
    ps = [0] * (DAY + 1)
    for i in range(DAY):
        ps[i + 1] = ps[i] + watchers[i]

    Q = int(input())
    out = []

    for _ in range(Q):
        s, e = parse_interval(input())
        total = cyclic_sum(ps, s, e)
        length = cyclic_len(s, e)
        out.append(f"{total / length:.10f}")

    print("\n".join(out))


if __name__ == "__main__":
    solve()