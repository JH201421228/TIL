import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(H, W):
    MOD = 1_000_000_007

    # 모든 가능한 창문의 수: H(H+1)/2 × W(W+1)/2
    total_windows = (H * (H + 1) // 2) * (W * (W + 1) // 2)

    # 모든 가능한 창문에서 제거되는 총 벽돌 수 계산
    # 각 위치 (i,j)에 있는 벽돌이 선택되는 경우의 수: i*(H-i+1) * j*(W-j+1)
    # 따라서 총 벽돌 수는 모든 위치에 대한 합: Σ(i=1 to H) Σ(j=1 to W) i*(H-i+1) * j*(W-j+1)
    # 이는 계산하면 H(H+1)(H+2)/6 * W(W+1)(W+2)/6 이 됨
    total_bricks = ((H * (H + 1) * (H + 2)) // 6) * ((W * (W + 1) * (W + 2)) // 6)

    # 평균 벽돌 수 = 총 벽돌 수 / 창문 수
    # 분수 a/b 형태로 표현하면:
    # 분자 a = total_bricks
    # 분모 b = total_windows

    # 최대공약수로 약분
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    g = gcd(total_bricks, total_windows)
    a = total_bricks // g
    b = total_windows // g

    # 모듈러 곱셈 역원 계산 (페르마의 소정리 이용)
    def mod_inverse(x, mod):
        return pow(x, mod - 2, mod)

    b_inverse = mod_inverse(b, MOD)

    # (a * b^(-1)) % MOD 계산
    result = (a * b_inverse) % MOD

    # 벽돌 하나 제거 비용 9원 곱하기
    result = (result * 9) % MOD

    return result


# 입력 처리
def main():
    H, W = map(int, input().split())
    print(solution(H, W))


if __name__ == "__main__":
    main()