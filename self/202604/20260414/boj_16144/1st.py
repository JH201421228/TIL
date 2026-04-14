import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    
    x1, y1 = 1, nums[0]
    x2, y2 = N, nums[N-1]+1
    
    a, b, c = x1-x2, y1-y2, x1*y2-x2*y1
    print(b/a, c/a)
    for i in range(1, N-1):
        x, y = i+1, nums[i]
        print(x, y, y+1)
        print(x, x*(b)/(a) + (c)/(a))
        
        if y <= x*(b)/(a) + (c)/(a) < y+1: continue
        else: break
    else:
        print("pass")
        return
    
    
    x1, y1 = 1, nums[0]+1
    x2, y2 = N, nums[N-1]
    
    a, b, c = x1-x2, y1-y2, x1*y2-x2*y1
    print(b/a, c/a)
    for i in range(1, N-1):
        x, y = i+1, nums[i]
        print(x, y, y+1)
        print(x, x*(b)/(a) + (c)/(a))
        if y <= x*(b)/(a) + (c)/(a) < y+1: continue
        else: break
    else:
        print("pass")
        return
    
    
    print("fail")
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()