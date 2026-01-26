import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    AA, BB = [], []
    ans = 0
    for idx in range(N):
        if A[idx] >= B[idx]:
            AA.append(A[idx]-B[idx])
            ans += A[idx]
        else:
            BB.append(B[idx]-A[idx])
            ans += B[idx]
            
    AA.sort(reverse=True)
    BB.sort(reverse=True)
    
    len_a, len_b = len(AA), len(BB)
    
    if abs(len_a - len_b) <= K:
        print(ans)
        return
    
    if len_a > len_b:
        while len_a - len_b > K:
            len_a -= 1
            len_b += 1
            ans -= AA.pop()
    else:
        while len_b - len_a > K:
            len_b -= 1
            len_a += 1
            ans -= BB.pop()
    
    print(ans)
    
    return


def main():
    for _ in range(int(input())):
        solve()

    return


if __name__ == "__main__":
    main()