import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
sams = list(map(int, input().split()))
# print(sams)

check_list = [0] * 200_000_001

for sam in sams:
    check_list[sam] = 1


delta = (-1, 1)
ans = 0
check_num = 0
multi = 0
while True:
    multi += 1
    for sam in sams:
        for dx in delta:
            if not check_list[sam + dx * multi]:
                check_list[sam + dx * multi] = 1
                ans += multi
                check_num += 1
                if check_num == K:
                    print(ans)
                    exit(1)
