import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


S = list(input().rstrip())
q = int(input())
q_list = [list(input().split()) for _ in range(q)]
# print(q_list)
length_S = len(S) + 1
for idx in range(length_S-1):
    S[idx] = ord(S[idx]) - ord('a')
# print(S)

matrix = [[0] * length_S for _ in range(26)]
for i in range(26):
    for j in range(1, length_S):
        if S[j-1] == i:
            matrix[i][j] = matrix[i][j-1] + 1
        else:
            matrix[i][j] = matrix[i][j-1]
# print(matrix)
for char, start, end in q_list:
    print(matrix[ord(char)-ord('a')][int(end)+1] - matrix[ord(char)-ord('a')][int(start)])
