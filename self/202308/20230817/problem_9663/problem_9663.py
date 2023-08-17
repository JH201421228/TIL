import sys
sys.stdin = open('input.txt')

def nq(N):
    if len(arr) == N:
        # print(arr)
        global cnt
        cnt += 1
        return

    for i in range(N):
        if not chess_board[i]:
            for j in range(len(arr)): #x, y /// j, arr[j] /// len(arr), i
                if j - len(arr) == arr[j] - i or j - len(arr) == i - arr[j]:
                    break
            else:
                chess_board[i] = i+1
                arr.append(i)
                nq(N)
                arr.pop()
                chess_board[i] = 0


N = int(input())
chess_board = [0] * N
arr = []
cnt = 0
# print(chess_board)
nq(N)
print(cnt)