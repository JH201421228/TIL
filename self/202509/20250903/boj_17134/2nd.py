import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline

MAXN = 1_000_000
PI = math.pi

# -------- sieve: 소수표 (2 제외) --------
def sieve(n: int):
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0] = 0; is_prime[1] = 0
    r = int(n ** 0.5)
    for i in range(2, r + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
    is_prime[2] = 0  # 홀수 소수만 쓸 거라 2는 제외
    return is_prime

# -------- bit-reversal 인덱스 --------
def bitrev_table(n: int):
    lg = (n.bit_length() - 1)
    rev = list(range(n))
    for i in range(n):
        x = i
        r = 0
        for _ in range(lg):
            r = (r << 1) | (x & 1)
            x >>= 1
        rev[i] = r
    return rev

# -------- 실/허수 분리 FFT --------
def fft_realimag(re, im, invert: bool, rev, n: int):
    # bit-reversal
    # swap only when i < rev[i]
    for i in range(1, n):
        j = rev[i]
        if i < j:
            re[i], re[j] = re[j], re[i]
            im[i], im[j] = im[j], im[i]

    k = 1
    while k < n:
        # w = exp(±i * pi / k)  (여기선 네 기존 공식을 그대로 사용)
        ang = (PI / k) if invert else -(PI / k)
        ca = math.cos(ang)
        sa = math.sin(ang)
        step = k << 1

        for i in range(0, n, step):
            wr = 1.0
            wi = 0.0
            # j = 0..k-1: (wr + i*wi)가 w^j
            for j in range(k):
                xr = re[i + j]
                xi = im[i + j]
                yr = re[i + j + k]
                yi = im[i + j + k]

                # y * wp
                tr = yr * wr - yi * wi
                ti = yr * wi + yi * wr

                # butterfly
                re[i + j]     = xr + tr
                im[i + j]     = xi + ti
                re[i + j + k] = xr - tr
                im[i + j + k] = xi - ti

                # wp *= w  (복소 곱)
                # (wr, wi) <- (wr*ca - wi*sa, wr*sa + wi*ca)
                nwr = wr * ca - wi * sa
                wi  = wr * sa + wi * ca
                wr  = nwr

        k <<= 1

    if invert:
        inv_n = 1.0 / n
        for i in range(n):
            re[i] *= inv_n
            im[i] *= inv_n

# -------- 컨볼루션 wrapper --------
def convolution_int(a, b):
    # a, b: 0/1 정수 리스트
    la = len(a); lb = len(b)
    n = 1
    need = la + lb - 1
    while n < need:
        n <<= 1

    # 실/허수 분리 버퍼
    re1 = [0.0] * n
    im1 = [0.0] * n
    re2 = [0.0] * n
    im2 = [0.0] * n

    # copy
    for i, v in enumerate(a):
        re1[i] = float(v)
    for i, v in enumerate(b):
        re2[i] = float(v)

    # bit-reversal 캐시
    rev = bitrev_table(n)

    # FFT
    fft_realimag(re1, im1, False, rev, n)
    fft_realimag(re2, im2, False, rev, n)

    # pointwise multiply: (re1 + i*im1) * (re2 + i*im2)
    for i in range(n):
        ar, ai = re1[i], im1[i]
        br, bi = re2[i], im2[i]
        re1[i] = ar * br - ai * bi
        im1[i] = ar * bi + ai * br

    # inverse FFT
    fft_realimag(re1, im1, True, rev, n)

    # 반올림하여 정수로
    res = [0] * need
    for i in range(need):
        # 안전 반올림
        v = re1[i]
        res[i] = int(v + 0.5) if v >= 0 else int(v - 0.5)
    return res

# -------- 문제별 벡터 구성 --------
def build_vectors():
    is_prime = sieve(MAXN)

    # A: 홀수 소수
    A = [0] * (MAXN + 1)
    for i in range(3, MAXN + 1, 2):
        if is_prime[i]:
            A[i] = 1

    # B: 짝수 세미소수 (4, 그리고 2*p)
    B = [0] * (MAXN + 1)
    B[4] = 1
    half = MAXN // 2
    for p in range(2, half + 1):
        if is_prime[p]:
            B[p << 1] = 1
    return A, B

def precompute():
    A, B = build_vectors()
    C = convolution_int(A, B)  # 길이 ~ 2*MAXN+1
    return C

def main():
    C = precompute()
    t = int(input())
    out_lines = []
    for _ in range(t):
        x = int(input())
        out_lines.append(str(C[x] if 0 <= x < len(C) else 0))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
