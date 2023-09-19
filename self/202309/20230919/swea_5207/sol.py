import sys
sys.stdin = open('input.txt')

# 조사 방향
def binary_search(L, R, K, D):
    global result
    # 중간값
    mid = (L + R) // 2
    # 중간 값의 위치가 == 대상이라면
    if A[mid] == K:
        # 좌우, 반복하면서 찾아낸 대상! 횟수 1 증가
        result += 1
        return
    # 타겟이 중간값보다 크면?
    elif A[mid] < T:
        # 이전번에 오른쪽에서 왔으면 종료
        if D == 'right':
            return
        # 오른쪽으로 조사 보낼것
        binary_search(mid + 1, R, K, 'right')
    # 타겟이 중간값보다 작으면?
    else:
        # 이전번에 왼쪽에서 왔으면 종료
        if D == 'left':
            return
        # 왼쪽으로 조사 보낼것
        binary_search(L, mid-1, K, 'left')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    # B 전수 조사
    result = 0
    for idx in range(M):
        binary_search(0, N-1, B[idx], 'start')

    print(f'#{tc} {result}')