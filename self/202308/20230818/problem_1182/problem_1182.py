import sys
sys.stdin = open('input.txt')


def why_do_this(ans, start, N, sum_val):

    if ans and sum(ans) == sum_val:
        global cnt
        cnt += 1
        return

    for i in range(start, N):
        # if numbers[i] not in ans:
        ans.append(numbers[i])
        why_do_this(ans, i+1, N, sum_val)
        ans.pop()


N, sum_val = map(int, input().split())
numbers = list(map(int, input().split()))
ans = []
cnt = 0
why_do_this(ans, 0, N, sum_val)
print(cnt)