import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def changer(N, circle):
    temp = []
    for idx in range(N):
        temp_dict = {'R': 0, 'G': 0, 'B': 0}
        l = circle[idx - 1]
        n = circle[idx]
        r = circle[idx+1] if idx < N-1 else circle[0]
        temp_dict[l] += 1
        temp_dict[n] += 1
        temp_dict[r] += 1
        if l == n and n == r or (temp_dict['B'] == 1 and temp_dict['G'] == 1):
            temp.append('B')
        elif (temp_dict['R'] == 2 and temp_dict['G'] == 1) or (temp_dict['G'] == 2 and temp_dict['B'] == 1) or (temp_dict['B'] == 2 and temp_dict['R'] == 1):
            temp.append('R')
        else:
            temp.append('G')

    return temp

N, K = map(int, input().split())
circle = list(input().rstrip())

for _ in range(K):
    circle = changer(N, circle)

r, g, b = 0, 0, 0
for c in circle:
    if c == 'R': r += 1
    elif c == 'G': g += 1
    else: b += 1

print(r, g, b)