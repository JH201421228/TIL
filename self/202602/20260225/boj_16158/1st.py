import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a%b
        
    return a


def ranges(x, p):
    a, b = (200*p - x*p), (x*p)
    return min(a, b), max(a, b)


def solve():
    N, X, K = map(int, input().split())
    
    sounds = list(map(int, input().split()))
    
    nums = []
    
    for s in sounds:
        a, b = ranges(X, s)
        nums.append((a, -1))
        nums.append((b, 1))
        
    nums.sort()
    
    cnt = 0
    cur = 0
    
    for idx in range(2*N):
        cnt -= nums[idx][1]
        cur = nums[idx][0]
        
        if cnt == K:
            if int(cur/100) == cur/100: print(cur//100)
            else:
                a = gcd(cur, 100)
                print(f"{cur//a}/{100//a}")
            return
    
    else:
        print(-1)
        return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()