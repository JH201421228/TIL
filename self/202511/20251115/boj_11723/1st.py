import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve(S):
    cmd = list(input().rstrip().split())
    
    if cmd[0] == "add":
        S[int(cmd[1])] = 1
    elif cmd[0] == "remove":
        S[int(cmd[1])] = 0
    elif cmd[0] == "check":
        print(S[int(cmd[1])])
    elif cmd[0] == "toggle":
        S[int(cmd[1])] = 1 - S[int(cmd[1])]
    elif cmd[0] == "all":
        for idx in range(1, 21): S[idx] = 1
    else:
        for idx in range(1, 21): S[idx] = 0
    
    return


def main():
    S = [0] * 21
    
    for _ in range(int(input())):
        solve(S)
    
    return


if __name__ == "__main__":
    main()