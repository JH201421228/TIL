import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = list(input())
q = int(input())
search_info = [list(input().split()) for _ in range(q)]
# print(search_info)

for char, start, end in search_info:
    cnt = 0
    for ss in S[int(start): int(end)+1]:
        if ss == char:
            cnt += 1
    print(cnt)