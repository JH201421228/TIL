import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    
    q1, q2, q3 = arr[:x], arr[x:y], arr[y:]
    
    m = min(q2)
    idx = q2.index(m)
    
    q4 = q1 + q3
    q5 = q2[idx:] + q2[:idx]
    
    pos = len(q4)
    
    for i in range(len(q4)):
        if q4[i] > m: 
            pos = i
            break
        
    print(*q4[:pos], *q5, *q4[pos:])
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()