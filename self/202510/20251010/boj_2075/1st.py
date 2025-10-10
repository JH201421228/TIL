import sys
import heapq
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    cur = []
    stacks = [[] for _ in range(N)]
    
    for _ in range(N):
        temp = list(map(int, input().split()))
        
        for idx in range(N):
            stacks[idx].append(temp[idx])
            
    for idx in range(N):
        heapq.heappush(cur, (-stacks[idx].pop(), idx))
        
    for _ in range(N):
        v, idx = heapq.heappop(cur)
        heapq.heappush(cur, (-stacks[idx].pop(), idx))
        
    print(-v)
    
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()