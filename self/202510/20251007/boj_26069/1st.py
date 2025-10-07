import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


tar_name = "ChongChong"
dance_dict = {tar_name: True}


def solve():
    ans = 1

    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if a in dance_dict or b in dance_dict:
            if a not in dance_dict:
                dance_dict[a] = True
                ans += 1
            if b not in dance_dict:
                dance_dict[b] = True
                ans += 1

    print(ans)

    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()