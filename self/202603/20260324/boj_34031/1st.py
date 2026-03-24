import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    A = input().rstrip()
    B = input().rstrip()
    A_dict = {}
    B_dict = {}
    
    trans = {"(": 1, ")": -1}
    
    cur = 0
    for a in A:
        cur += trans[a]
        if cur < 0: break
        
        A_dict[cur] = A_dict.get(cur, 0) + 1
        
    cur = 0
    tmp = 0
    for b in B:
        cur += trans[b]
        if trans[b] > 0: tmp += 1
        else: tmp = max(0, tmp-1)
        
        if not tmp: B_dict[cur] = B_dict.get(cur, 0) + 1
        
    ans = 0
    for k, v in A_dict.items():
        u = B_dict.get(-k, 0)
        ans += u*v
        
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()