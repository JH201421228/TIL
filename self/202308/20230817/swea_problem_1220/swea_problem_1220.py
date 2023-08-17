import sys
sys.stdin = open('input.txt')
# N극이 아래부분, S극이 윗부분 /// 1: N극, 2: S극
# 전위하면 N 왼쪽, S 오른쪽
for test_num in range(10):
    nothing = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(100)]
    trans_magnetic = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            trans_magnetic[i][j] = magnetic[j][i]