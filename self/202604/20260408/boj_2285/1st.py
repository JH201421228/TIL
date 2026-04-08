import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = []
    
    for _ in range(N):
        arr.append(list(map(int, input().split())))
        
    arr.sort(reverse=True)
    
    XAs = []
    while arr:
        x, a = arr.pop()
        if XAs and x == XAs[-1][0]: XAs[-1][1] += a
        else: XAs.append([x, a])
            
    N = len(XAs)
    weighted_sum = 0
    popularity = 0
    
    for idx in range(1, N):
        weighted_sum += (XAs[idx][0] - XAs[0][0]) * XAs[idx][1]
        popularity += XAs[idx][1]
        
    ans = XAs[0][0]
    ans_sum = weighted_sum
    
    right = weighted_sum
    right_popularity = popularity
    left = 0
    left_popularity = 0
    
    for idx in range(1, N):
        diff = XAs[idx][0] - XAs[idx-1][0]
        
        # print("turn: ", idx)
        
        left_popularity += XAs[idx-1][1]
        # print("left popularity: ", left_popularity)
        # print("prev left: ", left)
        left += left_popularity * diff
        # print("curr left: ", left)
        
        right_popularity -= XAs[idx][1]
        # print("right popularity: ", right_popularity)
        # print("prev right: ", right)
        right -= right_popularity * diff + XAs[idx][1] * diff
        # print("curr right: ", right)
        
        # print("-" * 100)
        
        if left + right < ans_sum:
            ans_sum = left + right
            ans = XAs[idx][0]
    
    print(ans)
    # print(ans_sum)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()