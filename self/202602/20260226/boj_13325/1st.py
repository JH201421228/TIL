import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def fix(K, depth, idx, arr):
    if depth == K:
        return arr[idx], arr[idx]
    
    l, ll = fix(K, depth+1, idx<<1, arr)
    r, rr = fix(K, depth+1, idx<<1|1, arr)
    
    return max(l, r) + arr[idx], ll+rr+abs(l-r)+arr[idx]  
    

def solve():
    K = int(input())
    arr = [0, 0] + list(map(int, input().split()))
    
    print(fix(K, 0, 1, arr)[1])
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()