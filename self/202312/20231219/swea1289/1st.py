import sys
sys.stdin = open('input.txt')

for t in range(int(input())):
    bi = input()
    ans = 0
    for idx in range(len(bi)-1):
        if bi[idx] != bi[idx+1]:
            ans += 1

    if bi[0] == '1':
        ans += 1

    print(f'#{t+1} {ans}')
