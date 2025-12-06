import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    s, e = 1, N
    ans_idx = 1
    
    while s <= e:
        mid = (s + e) >> 1
        
        print(f"? A {mid}",flush=True)
        a_res = int(input())
        
        print(f"? B {N-mid+1}",flush=True)
        b_res = int(input())
        
        if a_res < b_res:
            ans_idx = mid
            s = mid+1
        else:
            e = mid-1
    
    print(f"? A {ans_idx}",flush=True)
    a_res = int(input())
    
    print(f"? B {N-ans_idx}",flush=True)
    b_res = int(input())
    
    print(f"! {max(a_res, b_res)}")
    
    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()