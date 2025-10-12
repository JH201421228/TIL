import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    seq = list(map(int, input().split()))
    tar_n = int(input())
    
    i, j = 0, N-1
    
    seq.sort()
    
    ans = 0
    cur = seq[i] + seq[j]
    
    while True:
        if i >= j: break
        
        if cur > tar_n:
            cur -= seq[j]
            j -= 1
            try:
                cur += seq[j]
            except: break
            
        elif cur < tar_n:
            cur -= seq[i]
            i += 1
            try:
                cur += seq[i]
            except: break

        else:
            ans += 1
            i += 1
            j -= 1
            try:
                cur = seq[i] + seq[j]
            except: break
            
    print(ans)
    
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()