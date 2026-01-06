import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def score(cur, cur_state, change):
    res = 0
    cnt = 0
    
    for idx in range(5):
        if change[idx]:
            cur_state[cur[idx]] -= 1
            cnt += 1
        
    for n in range(6**cnt):
        temp = []
        tmp = 0
        for _ in range(cnt):
            temp.append(n%6 if n%6 else 6)
            n //= 6
        
        for k in temp:
            cur_state[k] += 1
            
        for k, v in cur_state.items():
            if v == 5:
                tmp = 50
                continue
            tmp = max(tmp, k*v)
            
        for k in temp:
            cur_state[k] -= 1
        
        res += tmp
        
    for idx in range(5):
        if change[idx]: cur_state[cur[idx]] += 1
        
    return res


def dfs(n, s, cur, cur_state, change, res):
    if not n: return max(res, score(cur, cur_state, change))
    
    for idx in range(s, 5):
        change[idx] = 1
        
        res = dfs(n-1, idx+1, cur, cur_state, change, res)
        
        change[idx] = 0
    
    return res


def solve():
    cur = list(map(int, input().split()))
    
    cur_state = {i:0 for i in range(1, 7)}
    for k in cur: cur_state[k] += 1
    
    change = [0] * 5
    
    ans = 0
    
    for i in range(6):
        ans = max(ans, dfs(i, 0, cur, cur_state, change, 0) * (6**(5-i)))
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()