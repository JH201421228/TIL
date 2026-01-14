import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    MOD = 1_000_000_007
    
    string_dict = {}
    for i in range(65, 91): string_dict[chr(i)] = 0
    for i in range(97, 123): string_dict[chr(i)] = 0
    
    N = int(input())
    string = input().rstrip()
    
    for s in string: string_dict[s] += 1
    
    ans = (N*(N-1)//2)
    ans %= MOD
    
    for k, v in string_dict.items():
        if v > 2:
            ans += pow(2, v, MOD)
            ans -= 1 + v + (v*(v-1)//2)
            ans %= MOD
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()