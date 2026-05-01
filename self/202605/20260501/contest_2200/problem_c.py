import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    string = input().rstrip()
    stack = []
    
    for s in string:
        if not stack: stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else: stack.append(s)
            
    if stack: print("NO")
    else: print("YES")
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()