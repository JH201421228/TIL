import sys
sys.stdin = open('input.txt')

paper = [50_000, 10_000, 5_000, 1_000, 500, 100, 50, 10]

for t in range(int(input())):
    money = int(input())
    print(f'#{t+1}')
    for p in paper:
        print(money // p, end=' ')
        money %= p
    print('')