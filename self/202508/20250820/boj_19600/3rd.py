import sys
import bisect
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 3^k 미리 준비 (2^63-1 < 3^40 이므로 3^40까지만)
POW3 = [1]
while POW3[-1] <= (1 << 63):
    POW3.append(POW3[-1] * 3)

def solve_one(N: int):
    # Binary: floor(log2 N) = bit_length - 1
    b = N.bit_length() - 1

    # Ternary:
    # k = floor_log3(N)  (POW3[k] <= N < POW3[k+1])
    k = bisect.bisect_right(POW3, N) - 1
    p = POW3[k]
    t = 2 * k + (1 if N >= 2 * p else 0)

    return b, t

def main():
    q = int(input())
    out_lines = []
    for _ in range(q):
        N = int(input())
        b, t = solve_one(N)
        out_lines.append(f"{b} {t}")
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
