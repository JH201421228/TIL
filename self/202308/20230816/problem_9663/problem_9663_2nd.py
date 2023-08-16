import sys
sys.stdin = open('input.txt')

def NQ(N, chess_line):
    if len(valuse) == N:
        print(valuse)
        global cnt
        cnt += 1
        return

    for i in range(N):
        if not chess_line[i][0] and not chess_line[i][1]:
            valuse.append(i)
            chess_line[i][0] = 1

            for j in range(N):
                if chess_line[j][1]:
                    chess_line[j][1] = 0
                    if j-1 >= 0:
                        chess_line[j-1][1] = 1
                    if j+1 < N:
                        chess_line[j+1][1] = 1

            if i-1 >= 0:
                chess_line[i-1][1] = 1
            if i+1 < N:
                chess_line[i+1][1] = 1
            print(valuse)
            NQ(N, chess_line)
            print(valuse)
            valuse.pop()


N = int(input())
chess_line = [[0, 0] for _ in range(N)]
cnt = 0
valuse = []
# print(chess_line)
NQ(N, chess_line)
# print(chess_line[0][0])