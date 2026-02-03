import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    D, N = map(int, input().split())
    
    dia = list(map(int, input().split()))

    for i in range(1, D):
        dia[i] = min(dia[i-1], dia[i])
    
    cand = list(map(int, input().split()))
    cand_idx = 0
    
    while dia:
        cur = dia.pop()
        
        if cand[cand_idx] <= cur: cand_idx += 1
        
        if cand_idx == N:
            print(len(dia)+1)
            return
    
    print(0)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()