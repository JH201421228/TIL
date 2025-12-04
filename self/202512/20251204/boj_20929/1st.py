import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    a_s, a_e, b_s, b_e = 1, N, 1, N
    
    while True:
        a_mid = (a_s + a_e) >> 1
        b_mid = (b_s + b_e) >> 1
        
        print(f"? A {a_mid}",flush=True)
        a_res = int(input())
        
        print(f"? B {b_mid}",flush=True)
        b_res = int(input())
        
        if a_mid == b_mid:
            print(f"! {a_mid}")
            break
        
        
    
    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()