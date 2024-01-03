import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for t in range(int(input())):
    ans = []
    for _ in range(int(input())):
        char, n = input().split()
        ans += char*int(n)
    print(f'#{t+1}')
    for i in range(len(ans)):
        print(ans[i], end='')
        if (i+1) % 10 == 0:
            print()
    print()