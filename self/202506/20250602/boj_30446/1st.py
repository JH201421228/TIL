import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def counter(n):
    res = 9
    for _ in range((n-1) // 2):
        res *= 10
    return res

def solve():
    N = int(input())
    N_str = str(N)
    ans = 0

    for n in range(1, len(N_str)):
        ans += counter(n)

    for idx in range((len(N_str)+1)//2):
        temp = (int(N_str[idx])-1 if not idx else int(N_str[idx])) * (10**(((len(N_str)+1)//2)-1-idx))
        if temp > 0: ans += temp

    N_list = list(N_str)
    for idx in range((len(N_str)+1)//2):
        N_list[-idx-1] = N_list[idx]
    if int(''.join(N_list)) <= N: ans += 1

    print(ans)

    return


if __name__ == "__main__":
    solve()