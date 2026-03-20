import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    if N < 7:
        print("NO")
        return
    
    print("YES")
    
    if N%2:
        ans = "1 + 4\n5 * 5\n2 + 7\n3 + 6\n9 * 9\n25 * 81"
        for i in range(8, N+1, 2): ans += f"\n{i+1} - {i}\n2025 * 1"
    else:
        ans = "1 + 8\n2 + 7\n9 * 9\n3 + 6\n9 - 4\n5 * 5\n25 * 81"
        for i in range(9, N+1, 2): ans += f"\n{i+1} - {i}\n2025 * 1"
            
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    solve()