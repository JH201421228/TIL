import sys
from collections import deque
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    n, x, y = map(int, input().split())
    
    q1, q2, q3 = deque([]), deque([]), deque([])
    
    arr = list(map(int, input().split()))
    
    for a in arr[:x]: q1.append(a)
    for a in arr[x:y]: q2.append(a)
    for a in arr[y:]: q3.append(a)
    
    standard = min(q2)
    
    while q1 and q1[-1] > standard: q3.appendleft(q1.pop())
    while q3 and q3[0] < standard: q1.append(q3.popleft())
    while q2[0] != standard: q2.append(q2.popleft())
    
    print(*q1, *q2, *q3)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()