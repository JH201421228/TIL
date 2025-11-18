import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def is_same_dot(d1, d2, d3, d4):
    if (d1 == d3 or
        d1 == d4 or
        d2 == d3 or
        d2 == d4):
        return True
    
    return False


def is_online(d1, d2, d3):
    if (d3[0] >= min(d1[0], d2[0]) and
        d3[1] <= max(d1[1], d2[1]) and
        (d1[1] - d3[1]) * (d2[0] - d3[0]) ==
        (d1[0] - d3[0]) * (d2[1] - d3[1])):
        return True
    
    return False


def ccw(d1, d2, d3, d4):
    
    expr1 = (d3[0] - d2[0]) * (d2[1] - d1[1]) - (d2[0] - d1[0]) * (d3[1] - d2[1])
    expr2 = (d4[0] - d2[0]) * (d2[1] - d1[1]) - (d2[0] - d1[0]) * (d4[1] - d2[1])
    expr3 = (d1[0] - d4[0]) * (d4[1] - d3[1]) - (d4[0] - d3[0]) * (d1[1] - d4[1])
    expr4 = (d2[0] - d4[0]) * (d4[1] - d3[1]) - (d4[0] - d3[0]) * (d2[1] - d4[1])
    
    if expr1 * expr2 < 0 and expr3 * expr4 < 0:
        return True
    
    return False


def cross_check(l1, l2):
    d1 = l1[:2]
    d2 = l1[2:]
    d3 = l2[:2]
    d4 = l2[2:]
    
    if is_same_dot(d1, d2, d3, d4):
        return True
    
    if is_online(d1, d2, d3):
        return True
    
    if is_online(d1, d2, d4):
        return True
    
    if is_online(d3, d4, d1):
        return True
    
    if is_online(d3, d4, d2):
        return True
    
    if ccw(d1, d2, d3, d4):
        return True
    
    return False


def travel(n, G, V):
    V[n] = 1
    q = deque([n])
    
    res = 0
    
    while q:
        n = q.popleft()
        res += 1
        
        for x in G[n]:
            if not V[x]:
                V[x] = 1
                q.append(x)
                
    return res


def solve():
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    
    G = [[] for _ in range(N+1)]
    
    for i in range(N):
        for j in range(i+1, N):
            if cross_check(lines[i], lines[j]):
                G[i+1].append(j+1)
                G[j+1].append(i+1)
    
    V = [0] * (N+1)
    
    cnt = 0
    res = 0
    
    for n in range(1, N+1):
        if not V[n]:
            cnt += 1
            res = max(res, travel(n, G, V))
            
    print(cnt)
    print(res)
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()