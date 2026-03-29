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
        
    half = total_num // 2 + 1
    
    cnt = [0] * (N+1)
    state = [[] for _ in range(N+1)]
    
    for idx in range(1, total_num+1):
        cnt[candidates[idx][0]] += 1
        state[candidates[idx][0]].append(idx)
    
    idxs = [0] * (total_num+1)
    max_val = 0
    min_val = min(cnt[1:])
    min_idxs = []
    
    for idx in range(1, N+1):
        if cnt[idx] > max_val:
            max_val = cnt[idx]
            max_idx = idx

        if cnt[idx] == min_val: min_idxs.append(idx)
            
    while True:
        if max_val >= half:
            print(num_to_name[max_idx])
            break
        else:
            for idx in min_idxs:
                cnt[idx] = float("inf")
                for s in state[idx]:
                    while True:
                        idxs[s] += 1
                        if cnt[candidates[s][idxs[s]]] != min_val:
                            cnt[candidates[s][idxs[s]]] += 1
                            break
                            
                    if cnt[candidates[s][idxs[s]]] > max_val: 
                        max_val += 1
                        max_idx = candidates[s][idxs[s]]
                    
                state[idx] = []
                
            min_val = min(cnt[1:])
            min_idxs = []
                
            for idx in range(1, N+1):
                if cnt[idx] == min_val: min_idxs.append(idx)
            
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
