import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    L = int(input())
    S = input().rstrip()
    
    preprocess = [0] * L
    
    stack_n = 0
    
    for idx in range(1, L):
        while (stack_n and S[stack_n] != S[idx]):
            stack_n = preprocess[stack_n-1]
            
        if S[stack_n] == S[idx]:
            stack_n += 1
            preprocess[idx] = stack_n
            
    print(L - preprocess[-1])
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()