import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def isCCW(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)


def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    ans = 0
    value = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if i == j: continue
            if abs(i-j) == 1:
                tmp += 1
                continue
            
            if i > j:
                for cur in range(j+1, i):
                    if isCCW(i, arr[i], cur, arr[cur], j, arr[j]) >= 0: break
                else: tmp += 1
            else:
                for cur in range(i+1, j):
                    if isCCW(i, arr[i], cur, arr[cur], j, arr[j]) <= 0: break
                else: tmp += 1
                
        if tmp > value:
            value = tmp
            ans = i
            
    print(value)
            
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    solve()