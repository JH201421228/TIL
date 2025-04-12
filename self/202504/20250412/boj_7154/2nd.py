import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

satisfaction = [(4, 3, 2, 1), (8, 7, 6, 5), (12, 11, 10, 9)]

while True:
    N, M = map(int, input().split())
    if not N and not M:
        break

    ans, src, sink = 0, N + M + 1, N + M + 2
    G = [[] for _ in range(sink + 1)]
    F = [[0] * (sink + 1) for _ in range(sink + 1)]
    C = [[0] * (sink + 1) for _ in range(sink + 1)]
    D = [[0] * (sink + 1) for _ in range(sink + 1)]

    # Connect job positions to sink
    for i in range(N):
        job_node = i + M + 1
        capacity = int(input())
        C[job_node][sink] = capacity
        G[job_node].append(sink)
        G[sink].append(job_node)

    # Process student preferences
    for i in range(M):
        student_node = i + 1

        # Connect source to student
        C[src][student_node] = 1
        G[src].append(student_node)
        G[student_node].append(src)

        # Process student preferences
        temp = list(map(int, input().split()))
        grade = temp[0]
        for idx in range(1, 5):
            job_node = temp[idx] + M + 1
            G[student_node].append(job_node)
            G[job_node].append(student_node)
            # Negative cost for forward edges to make this a max flow problem
            D[student_node][job_node] = -satisfaction[grade - 1][idx - 1]
            D[job_node][student_node] = satisfaction[grade - 1][idx - 1]  # Reverse edge
            C[student_node][job_node] = 1

    # MCMF Algorithm
    while True:
        pre = [-1] * (sink + 1)
        dist = [float("inf")] * (sink + 1)
        inq = [False] * (sink + 1)  # Keep track of nodes in queue

        q = deque([src])
        dist[src] = 0
        inq[src] = True

        while q:
            n = q.popleft()
            inq[n] = False  # Remove from queue

            for x in G[n]:
                # If there's remaining capacity and we find a better path
                if C[n][x] > F[n][x] and dist[x] > dist[n] + D[n][x]:
                    dist[x] = dist[n] + D[n][x]
                    pre[x] = n

                    # Add to queue if not already in queue
                    if not inq[x]:
                        q.append(x)
                        inq[x] = True

        # If no path to sink, we're done
        if pre[sink] == -1:
            break

        n = sink
        while n != src:
            p = pre[n]
            F[p][n] += 1
            F[n][p] -= 1
            ans += D[p][n]
            n = p

    print(-ans)  # Print negative cost to get maximum satisfaction