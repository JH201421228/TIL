
def backtrackin(arr, now, end, result):
    # 후보군 목록
    # 부분집합의 원소로 now 번째의 값을 T/F (쓴다/안쓴다)
    c = [0] * 2
    # 언제까지 조사를 할 것이냐.
    if now == end:
        pass
    else:
        # 아직 조사해야하는 원소가 남았다.
        # 다음 원소를 조사 하러 가기 위해 index 1 증가
        now += 1
        # now

# 유망성 : 다음 조사를 하는 의미가 있니 없니?
# 후보군 수
MAXCANDIDATE = 12
# 대 원소 개수
NMAX = 12
data = list(range(11))
arr = [0] * NMAX # 각 원소를 사용할 것이냐 말 것이냐를 체크할 배열
backtrackin(arr, 0, 10, 0)