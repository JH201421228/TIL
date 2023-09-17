import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(M)]
print(board)