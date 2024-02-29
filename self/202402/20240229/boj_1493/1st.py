import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def div_box(a, b, c):
    if not a or not b or not c:
        return
    if a == 1 or b == 1 or c == 1:
        my_list[0] += a * b * c
        return

    l = min(a, b, c)
    h = max(a, b, c)
    m = a + b + c - l - h

    idx = 1
    while l >= 2 ** (idx+1):
        idx += 1

    min_val = 2 ** idx
    my_list[idx] += (h // min_val) * (m // min_val)
    l_ = l - min_val
    h_ = h % min_val
    m_ = m % min_val

    div_box(min_val, m - m_, h_)
    div_box(l_, m - m_, h)
    div_box(min_val, m_, h)
    div_box(l_, m_, h)


l, w, h = map(int, input().split())
N = int(input())
cube_list = [0] * 21
my_list = [0] * 21
for _ in range(N):
    i, n = map(int, input().split())
    cube_list[i] = n
div_box(l, w, h)
# print(my_list)
# print(cube_list)

ans = 0
for i in range(20, 0, -1):
    if my_list[i] <= cube_list[i]:
        ans += my_list[i]
    else:
        ans += cube_list[i]
        my_list[i-1] += 8 * (my_list[i] - cube_list[i])

if my_list[0] > cube_list[0]:
    print(-1)
else:
    print(ans + my_list[0])