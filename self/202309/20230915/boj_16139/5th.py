import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
while True:
    pass
S = list(input().rstrip())
q = int(input())
search_info = [list(input().split()) for _ in range(q)]
# print(search_info)
check_char = search_info[0][0]
cnt = 0
SS = [0] * (1 + len(S))
for idx in range(len(S)):

    if check_char == S[idx]:
        cnt += 1
        SS[idx+1] = cnt
    else:
        SS[idx+1] = cnt
# print(SS)
for char, start, end in search_info:
    print(SS[int(end)+1]-SS[int(start)])
    # print(int(end)+1, start)

