import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, M, T = map(int, input().split())
    
    info = {}
    
    for i in range(N):
        info[i+1] = tuple(map(int, input().split()))
    
    time_stamp = []
    
    for _ in range(M):
        u, v = map(int, input().split())
        
        us, vs = info[u], info[v]
        
        if us[0] >= vs[1] or vs[0] >= us[1]: continue
        
        time_stamp.append((max(us[0], vs[0]), min(us[1], vs[1])))
    
    ans = [0] * (T+1)
    
    for time in time_stamp:
        ans[time[0]] += 1
        ans[time[1]] -= 1
        
    for idx in range(1, T):
        ans[idx] += ans[idx-1]
        
    print('\n'.join(map(str, ans[:T])))
    
    return


def main():
    solve()
    
    return



if __name__ == "__main__":
    main()