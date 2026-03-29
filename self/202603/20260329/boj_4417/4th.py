import sys
input = sys.stdin.readline


def solve():
    N = int(input())

    num_to_name = {}
    for i in range(1, N + 1):
        num_to_name[i] = input().rstrip()

    is_available = [1] * (N + 1)

    total_num = 0
    candidates = [()]
    while True:
        line = input()
        if not line:
            break
        candidate = tuple(map(int, line.split()))
        if not candidate:
            break
        candidates.append(candidate)
        total_num += 1

    half = total_num // 2 + 1

    cnt = [0] * (N + 1)
    state = [[] for _ in range(N + 1)]

    # 초기 1순위 집계
    for idx in range(1, total_num + 1):
        first = candidates[idx][0]
        cnt[first] += 1
        state[first].append(idx)

    idxs = [0] * (total_num + 1)   # 각 투표지가 현재 가리키는 순위 인덱스

    while True:
        alive = [i for i in range(1, N + 1) if is_available[i]]

        max_val = max(cnt[i] for i in alive)
        min_val = min(cnt[i] for i in alive)

        # 과반 승자
        if max_val >= half:
            for i in alive:
                if cnt[i] == max_val:
                    print(num_to_name[i])
                    return

        # 전원 동률
        if max_val == min_val:
            for i in alive:
                print(num_to_name[i])
            return

        min_idxs = [i for i in alive if cnt[i] == min_val]

        # 같은 라운드에서 탈락하는 후보들 먼저 전부 비활성화
        for idx in min_idxs:
            is_available[idx] = 0

        # 탈락 후보들의 표 재분배
        for idx in min_idxs:
            for s in state[idx]:
                while True:
                    idxs[s] += 1
                    if idxs[s] >= len(candidates[s]):
                        break

                    nxt = candidates[s][idxs[s]]
                    if is_available[nxt]:
                        cnt[nxt] += 1
                        state[nxt].append(s)
                        break

            cnt[idx] = 0
            state[idx] = []


def main():
    solve()


if __name__ == "__main__":
    main()