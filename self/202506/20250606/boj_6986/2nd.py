import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solve():
    N, K = map(int, input().split())
    arr = [float(input()) for _ in range(N)]
    arr.sort()

    # 절사평균
    trim_mean = sum(arr[K:N-K]) / (N - 2 * K)

    # 보정평균
    corrected_arr = arr[:]
    for i in range(K):
        corrected_arr[i] = arr[K]
        corrected_arr[N - 1 - i] = arr[N - K - 1]
    correction_mean = sum(corrected_arr) / N

    # 출력
    print(f"{trim_mean + 1e-8:.2f}")
    print(f"{correction_mean + 1e-8:.2f}")

if __name__ == "__main__":
    solve()
