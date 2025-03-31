import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solve(n):
    next_gens = [0] * 26
    ans, ans_list = 0, []

    for i in range(n):
        for j in range(n):
            if i == j: continue
            a, b = ord(gens[i][0]), ord(gens[j][1])
            next_gens[max(a, b)-65] += 1

    for i in range(26):
        if next_gens[i]:
            ans += 1
            ans_list.append(chr(i+65))

    print(ans)
    print(*ans_list)

    return


N = int(input())
gens = list(input().rstrip().split())

solve(N)