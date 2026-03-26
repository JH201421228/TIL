import sys
from itertools import combinations
sys.stdin = open("input.txt")
input = sys.stdin.readline


def recur(n, v):
    tmp = 0
    for nn in n:
        if int(nn) % 2: tmp += 1
        
    if len(n) == 1:
        global min_ans, max_ans
        min_ans = min(min_ans, v+tmp)
        max_ans = max(max_ans, v+tmp)
        return
    
    elif len(n) == 2:
        recur(str(int(n[0]) + int(n[1])), v+tmp)
    
    else:
        candidates = list(combinations(range(1, len(n)), 2))
        
        for i, j in candidates:
            recur(str(int(n[:i]) + int(n[i:j]) + int(n[j:])), v+tmp)
            

def solve():
    N = input().rstrip()
    
    global min_ans, max_ans
    min_ans, max_ans = float("inf"), -float("inf")
    
    recur(N, 0)
    
    print(min_ans, max_ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
    