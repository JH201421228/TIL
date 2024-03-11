import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
sams = list(map(int, input().split()))

delta = (-1, 1)

cordinate = [*sams]
multi = 0
ans = 0
check = 0
while True:
    multi += 1
    for sam in sams:
        for dx in delta:
            if sam + dx * multi not in cordinate:
                cordinate.append(sam + dx * multi)
                ans += multi
                check += 1
                if check == K:
                    print(ans)
                    exit(1)