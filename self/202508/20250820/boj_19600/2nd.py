import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())

    if N == 1:
        print(0, 0)
        return

    # 이진 탐색: 최악의 경우는 리프 노드까지 가는 것
    # 각 재귀 호출에서 1개의 원소(mid)를 확인
    binary_max = 0
    temp = N
    while temp > 1:
        temp //= 2
        binary_max += 1

    # 삼진 탐색: 각 재귀 호출에서 최대 2개 원소 확인
    # (left_third와 right_third)
    ternary_max = 0
    temp = N
    while temp > 1:
        ternary_max += 2  # 각 단계에서 2개 확인
        # 가장 큰 부분 구간의 크기로 이동
        # ternary search에서 3등분할 때 가장 큰 부분의 크기
        temp = (temp - 1) // 3
        if temp == 0:
            temp = 1

    print(binary_max, ternary_max)


def main():
    Q = int(input())
    for _ in range(Q):
        solve()


if __name__ == "__main__":
    main()