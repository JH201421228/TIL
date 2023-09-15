import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

S = list(input().rstrip())
q = int(input())
search_info = [list(input().split()) for _ in range(q)]
# print(search_info)

# for idx in range(len(S)):
#     S[idx] = ord(S[idx]) - ord('a')
# print(S)
# check_char_num = ord(search_info[0][0]) - ord('a')
for char, start, end in search_info:
    cnt = 0
    for ss in S[int(start): int(end)+1]:
        if ss == char:
            cnt += 1
    print(cnt)