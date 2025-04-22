import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 입력 받기
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# 무한대 값 설정
INF = float('inf')
min_area = INF

# 각 가능한 (left, bottom) 및 (right, top) 쌍에 대해 정사각형 생성 및 확인
for left_x in range(N):
    for right_x in range(N):
        for bottom_y in range(N):
            for top_y in range(N):
                x1, _ = points[left_x]
                x2, _ = points[right_x]
                _, y1 = points[bottom_y]
                _, y2 = points[top_y]

                # x1 < x2, y1 < y2 보장
                if x1 >= x2 or y1 >= y2:
                    continue

                # 정사각형 만들기
                side = max(x2 - x1, y2 - y1)
                square_x2 = x1 + side
                square_y2 = y1 + side

                # 내부 점 개수 세기
                inside_count = 0
                for x, y in points:
                    if x1 < x < square_x2 and y1 < y < square_y2:
                        inside_count += 1

                # 조건 검사
                if inside_count >= N - 2:
                    min_area = min(min_area, side * side)

# 결과 출력
print(min_area)