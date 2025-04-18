import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    N, K = map(int, input().split())
    a, b, c = 0.5 * K, 0.5 * K, -N+1
    day = int((-b + (b**2 - 4*a*c)**0.5) / (2*a))
    distance = int(0.5*K*((int(day)**2 + int(day))))

    ans = []

    if N-1 == distance: ans.append(int((-1)**(day-1) * ((day+1)//2) * K))
    else: ans.append(int((-1)**(day-1) * ((day+1)//2) * K + (-1) ** day * (N-1-distance)))

    if day % 2: ans.append('L')
    else: ans.append('R')

    print(*ans)