import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    A = list(map(int, input().split()))
    
    arr = [[-1, -1]]
    len_arr = 1
    
    for a in A:
        temp = []
        for _ in range(30):
            temp.append(a%2)
            a>>=1
        
        cur = 0
        
        while temp:
            o = temp.pop()
            
            if arr[cur][o] == -1:
                arr[cur][o] = len_arr
                arr.append([-1, -1])
                len_arr += 1
                
            cur = arr[cur][o]
    
    ans = 0
        
    for a in A:
        temp = []
        for _ in range(30):
            temp.append(a%2)
            a>>=1

        tmp = 0
        cur = 0
        for idx in range(29, -1, -1):
            n = temp[idx]
            if arr[cur][1-n] != -1:
                tmp += 1<<(idx)
                cur = arr[cur][1-n]
            else: cur = arr[cur][n]
            
        ans = max(tmp, ans)
        
    print(ans)

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()