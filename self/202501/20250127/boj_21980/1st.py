import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    N, K = map(int, input().split())
    S = list(map(str, input().split()))

    simillar = dict()

    for i in range(N):
        k2 = 0
        for c in S[i]:
            if ord(c) < 91:
                k2 += 1

        k1 = ''.join(sorted(list(S[i].lower())))
        simillar[(k1, k2)] = simillar.get((k1, k2), 0) + 1

    ans = 0
    for v in simillar.values():
        ans += ((v * (v-1)) >> 1)

    print(ans)