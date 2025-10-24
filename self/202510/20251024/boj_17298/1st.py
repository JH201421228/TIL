import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    ans = [-1] * N
    cur_idx = N-1
    
    temp = []
    
    while len(arr) > 1:
        cur_idx -= 1
        cur = arr.pop()
        
        if cur > arr[-1]:
            temp.append(cur)
        else:
            while temp and temp[-1] <= arr[-1]:
                temp.pop()
                
        if temp:
            ans[cur_idx] = temp[-1]
            
    
    print(*ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()