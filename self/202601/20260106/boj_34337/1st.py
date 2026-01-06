import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def score(cur, n):
    cur_state = {i: 0 for i in range(1, 7)}
    
    for idx in range(5):
        if idx == n: continue
        
        cur_state[cur[idx]] += 1
        
    res = 0
    for i in range(1, 7):
        cur_state[i] += 1
        
        tmp = 0
        
        for k, v in cur_state.items():
            tmp = max(tmp, k*v)
            
            if v == 5: tmp = 50
        
        cur_state[i] -= 1
        
        res += tmp
        
    return res


def solve():
    cur = list(map(int, input().split()))
    
    cur_state = {i: 0 for i in range(1, 7)}
    
    for k in cur: cur_state[k] += 1
    
    ans = 0
    
    print(cur_state)
    
    for k, v in cur_state.items():
        if v == 5:
            print(50 * (6**5))
            return
        
        ans = max(ans, k*v*6)
    
    
    for n in range(5):
        ans = max(ans, score(cur, n))
        
    print(ans * (6**4))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()