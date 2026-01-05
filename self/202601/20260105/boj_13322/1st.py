import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    string = input().rstrip()
    S = len(string)
    
    ans = [(string[:S-i], S-i-1) for i in range(len(string))]
    
    ans.sort()
    
    for _, a in ans:
        print(a)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()