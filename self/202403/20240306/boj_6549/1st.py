import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


while True:
    heights = list(map(int, input().split()))

    if not heights[0]:
        break

    stack = []
    ans = 0
    width = 0
    for idx in range(len(heights)):
        if not stack:
            stack.append((idx, heights[idx]))
            ans = max(ans, heights[idx])
        else:
            if stack[-1] > heights[idx]:
                stack.append((idx, heights[idx]))
            else:
                stack.append((idx, heights[idx]))
                ans = max(ans, stack[0])

