import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    x, y = map(int, input().split())
    
    if x > y:
        print("NO")
        return
    
    if not (x + y) % 2 and x == 0:
        print("NO")
        return
    
    print("YES")
    if (x+y) % 2: cut = 2*x+1
    else: cut = 2*x
    
    for i in range(1, cut):
        print(i, i+1)
        
    for i in range(cut, x+y):
        print(1, i+1)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()