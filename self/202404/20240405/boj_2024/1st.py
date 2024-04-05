import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


M = int(input())
lines = []
while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    if b <= 0:
        continue
    if a >= M:
        continue
    lines.append((a, b))
lines.sort(key=lambda x: -x[0])
# print(lines)

# 시작점은 포인트보다 작고 끝점은 포인트보다 큰 값중 최대값을 선정
# 시작점이 포인트보다 커지면 포인티를 최대값으로 변경
# 쵀대값이 설정되지 않으면 선분을 덮을 수 없으므로 0출력

point = 0
ans = 0
while lines:
    m_val = 0
    while True:
        if lines and lines[-1][0] <= point:
            a, b = lines.pop()
            m_val = max(m_val, b)
        else:
            if m_val:
                point = m_val
                ans += 1
                if point >= M:
                    print(ans)
                    exit(0)
                break
            else:
                print(0)
                exit(0)
print(0)

