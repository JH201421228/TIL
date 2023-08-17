import sys
sys.stdin = open('input.txt')

def NQ():
    if len(arr) == N:
        print(arr)
        global cnt
        cnt += 1
        return

    for i in range(N):
        if not chess_line[i][0] and not chess_line[i][1]:


N = int(input())
chess_line = [[0]*2 for _ in range(N)]
arr = []
cnt = 0
print(chess_line)