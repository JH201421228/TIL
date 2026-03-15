import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    stairs = [float("inf")] * (N+1)
    stairs[0] = 0
    
    for idx in range(N+1):
        if stairs[idx] < K:
            if idx+1 < N+1: stairs[idx+1] = min(stairs[idx]+1, stairs[idx+1])
            if idx + idx//2 < N+1: stairs[idx+idx//2] = min(stairs[idx]+1, stairs[idx+idx//2])
    
    if stairs[-1] != float("inf"): print("minigimbob")
    else: print("water")
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()