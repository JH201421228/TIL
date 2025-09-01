import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def available_init(n, state, k, clo):
    threshold_n = len(state) - 1

    cur = threshold_n
    cnt = 0
    while True:
        cur -= n
        cnt += 1

        if cnt > k:
            return False

        if cur <= 1: return True

        if state[cur]:
            threshold_n = cur
            continue
        else:
            cur = clo[cur]

        if cur >= threshold_n:
            return False


def solve():
    N, K = map(int, input().split())
    state = [0] + list(map(int, input().split()))
    closest_day = [*state]

    cur = 0
    for idx in range(N, -1, -1):
        if state[idx]:
            closest_day[idx] = idx
            cur = idx
        else:
            closest_day[idx] = cur

    s, e = 1, N-1
    while s <= e:
        mid = (s+e) >> 1

        if available_init(mid, state, K, closest_day):
            e = mid-1
        else:
            s = mid+1

    print(s)

    return


if __name__ == "__main__":
    solve()