import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def sorted_combination(arr):
    res = []

    for i in range(1<<len(arr)):
        tmp = 0
        for j in range(len(arr)):
            if i & (1<<j): tmp += arr[j]
        res.append(tmp)

    res.sort()

    return res


def solve(u, v, C):
    
    res = 0

    for n in u:
        s, e = 0, len(v)-1
        while s <= e:
            mid = (s+e) >> 1

            if n + v[mid] <= C:
                s = mid+1
            else:
                e = mid-1
        res += s

    print(res)

    return


def main():
    N, C = map(int, input().split())
    things = list(map(int, input().split()))

    solve(sorted_combination(things[:N//2]), sorted_combination(things[N//2:]), C)

    return


if __name__ == "__main__":
    main()