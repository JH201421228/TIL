import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    mem = [float("inf")] * N
    mem[0] = 0

    for i in range(N-1):
        for j in range(i+1, N):
            charge = (j-i)*(1+abs(arr[i]-arr[j]))

            mem[j] = min(mem[j], max(mem[i], charge))

    print(mem[-1])

    return


if __name__ == "__main__":
    solve()