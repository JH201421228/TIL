import sys
sys.stdin = open('input.txt')


def insane_func(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        # a = 20
        # b = 20
        # c = 20
        return 1048576
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                if i < j and j < k:
                    is_it_okay[i][j][k] = is_it_okay[i][j][k - 1] + is_it_okay[i][j - 1][k - 1] - is_it_okay[i][j - 1][k]
                else:
                    is_it_okay[i][j][k] = is_it_okay[i - 1][j][k] + is_it_okay[i - 1][j - 1][k] + is_it_okay[i - 1][j][k - 1] - is_it_okay[i - 1][j - 1][k - 1]
    return is_it_okay[a][b][c]

input_val = []
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    input_val.append([a, b, c])
# print(input_val)
is_it_okay = [[[0] * 21 for _ in range(21)] for _ in range(21)]
for i in range(20):
    for j in range(20):
        for k in range(20):
            if not i or not j or not k:
                is_it_okay[i][j][k] = 1
# print(is_it_okay)

for a, b, c in input_val:
    print(f'w({a}, {b}, {c}) = {insane_func(a, b, c)}')


