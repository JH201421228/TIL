import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


while True:
    recs = list(map(int, input().split()))
    if len(recs) == 1 and not recs[0]:
        break
    stack = []
    ans = 0
    for idx in range(1, len(recs)):
        if not stack:
            stack.append((idx, recs[idx]))
        else:
            if stack[-1][1] <= recs[idx]:
                stack.append((idx, recs[idx]))
            else:
                while stack:
                    i, h = stack.pop()
                    if stack:
                        s = stack[-1][0] + 1
                    else:
                        s = 1
                    ans = max(ans, (idx - s) * h)
                    if not stack or stack[-1][1] <= recs[idx]:
                        stack.append((idx, recs[idx]))
                        break
    while stack:
        i, h = stack.pop()
        if stack:
            s = stack[-1][0] + 1
        else:
            s = 1
        ans = max(ans, (recs[0] - s + 1) * h)
    print(ans)