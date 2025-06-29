import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())

    s1, s2, s3, pre, load = [n for n in range(N, 1, -1)], [], [], 0, 0
    s = [s1, s2, s3]
    if N % 2:
        s3.append(1)
        pre = 2
    else:
        s2.append(1)
        pre = 1

    for _ in range(K-1):
        temp, val = 0, 0
        for idx in range(3):
            if idx != pre and s[idx] and s[idx][-1] > val:
                val = s[idx][-1]
                temp = idx

        tmp, val = -1, float("inf")
        for idx in range(3):
            if idx != temp:
                if not s[idx]:
                    tmp = idx
                    break
                if s[idx][-1] > s[temp][-1] and val > s[idx][-1]:
                    val = s[idx][-1]
                    tmp = idx

        if tmp != -1:
            s[tmp].append(s[temp].pop())
            pre = tmp
            load = temp
            continue

        temp = 3 - temp - pre

        tmp, val = -1, float("inf")
        for idx in range(3):
            if idx != temp:
                if not s[idx]:
                    tmp = idx
                    break
                if s[idx][-1] > s[temp][-1] and val > s[idx][-1]:
                    val = s[idx][-1]
                    tmp = idx

        s[tmp].append(s[temp].pop())
        pre = tmp
        load = temp

    print(load+1, pre+1)
    return


if __name__ == "__main__":
    solve()