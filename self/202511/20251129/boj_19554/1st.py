import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    s, e = 1, N
    
    while True:
        mid = (s+e) >> 1
        print(f"? {mid}", flush=True)
        
        r = int(input())
        
        if r > 0: e = mid - 1
        elif r < 0: s = mid + 1
        else: break
        
    print(f"= {mid}")
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()