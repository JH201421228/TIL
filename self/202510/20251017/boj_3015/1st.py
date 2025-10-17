import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    S = []
    ans = 0

    for idx in range(N):
        if S:
            ans += 1
            cur = arr[idx]
            cur_cnt = 1

            while S and S[-1][0] <= cur:
                if S[-1][0] < cur:
                    v, u = S.pop()
                    if S:
                        ans += u
                    else:
                        ans += u-1
                else:
                    v, u = S.pop()
                    if S:
                        ans += u
                    else:
                        ans += u-1

                    cur_cnt += u
                    break
            
            S.append((cur, cur_cnt))

        else:
            S.append((arr[idx], 1))
    
    print(ans)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()