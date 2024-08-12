import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def area():
    ans = 0

    for idx in range(1, N+2):
        while (stack and arr[stack[-1]] > arr[idx]):
            i = stack.pop()
            ans = max(ans, arr[i] * (idx-stack[-1]-1))

        stack.append(idx)

    return ans


N = int(input())
arr = [0]
stack = [0]
for _ in range(N):
    arr.append(int(input()))
arr.append(0)

print(area())