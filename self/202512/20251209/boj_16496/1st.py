import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def padding(n, k):
    if not n:
        return n, k
    
    res = str(n)
    
    while len(res) < 10:
        res += res[-1]
    
    return int(res), k


def solve():
    N = int(input())
    temp = list(map(int, input().split()))
    
    padded = [padding(temp[i], i) for i in range(N)]
    padded.sort(reverse=True)
    
    ans = ''
    for _, idx in padded:
        ans += str(temp[idx])
       
    if ans[0] == '0':
        print(0)
    else:
        print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()