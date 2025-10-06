import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N = int(input())
    cnt_dic = {}
    ans = 0

    for _ in range(N):
        tmp = input().rstrip()

        if tmp == "ENTER":
            cnt_dic = {}

        else:
            if tmp in cnt_dic:
                continue
            else:
                cnt_dic[tmp] = 1
                ans += 1

    print(ans)

    return


def main():
    solve()
    return



if __name__ == "__main__":
    main()