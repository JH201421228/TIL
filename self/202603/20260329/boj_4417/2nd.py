import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    num_to_name = {}
    for i in range(1, N+1):
        num_to_name[i] = input().rstrip()
    
    is_available = [1] * (N+1)
    
    total_num = 0
    candidates = [(), ]
    while True:
        candidate = tuple(map(int, input().split()))
        if not candidate: break
        candidates.append(candidate)
        total_num += 1
        
    half = round((total_num+1)/2)
    
    cnt = [0] * (N+1)
    state = [[] for _ in range(N+1)]
    
    for idx in range(1, total_num+1):
        cnt[candidates[idx][0]] += 1
        state[candidates[idx][0]].append(idx)
    
    idxs = [0] * (total_num+1)
    while True:
        cur = max(cnt)
        
        if cur >= half:
            print(num_to_name[cnt.index(max(cnt))])
            break
        else:
            idx = cnt.index(min(cnt[1:]))
            is_available[idx] = 0

        min_idx = cnt.index(min(cnt[1:]))
        cnt[min_idx] = 0
        for man in state[min_idx]:
            idxs[man] += 1
            cnt[candidates[man][idxs[man]]] += 1
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
