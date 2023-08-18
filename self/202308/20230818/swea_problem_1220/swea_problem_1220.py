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

    # N극을 만난 상태에서 S극을 만난 뒤 다시 N극을 만나는 시점에서 +1
    cnt = 0
    for inner_list in trans_magnetic:
        status = 0 # 리셋 상태
        for i in range(100):
            block = inner_list[i]
            if block == 1: # N극을 만나면
                if not status or status == 1: # 처음 N을 만나거나 N을 만난뒤 다시 N을 만난다면
                    status = 1 # 마지막으로 N을 만난 상태
            elif block == 2 and (status == 1 or status == 2): # 마지막으로 N극을 만난 상태에서 S극을 만나거나 N극을 만난 상태에서 S극을 만난다면
                status = 2
            elif block == 1 and status == 2: # N극을 만난 뒤 S극을 만나고 N극을 만나게 된다면
                if not inner_list[i-1]: # 마지막으로 S극을 만나고 공백 뒤에 N극을 만나면
                    cnt += 1
                    status = 1 # 마지막으로 N을 만난 상태

    print(cnt)