import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    nums = list(map(int, input().split()))
    ans = 0
    
    while 1:
        if nums[0] == nums[1] or nums[1] == nums[-1] or nums[0] == nums[-1]: break
        
        nums.sort()
        nums[0] += 1
        nums[-1] -= 1
        ans += 1
        
    
    print(ans)
        
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()