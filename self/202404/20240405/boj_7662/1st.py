import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


for _ in range(int(input())):
    pq = []
    reverse_pq = []
    cnt = 0
    preD = 0
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if a == 'I':
            heapq.heappush(pq, int(b))
            heapq.heappush(reverse_pq, -int(b))
            cnt += 1
            print(pq, reverse_pq)
        else:
            if not cnt:
                pq, reverse_pq = [], []
            elif int(b) == 1:
                heapq.heappop(reverse_pq)
                preD = 1
                cnt -= 1
            else:
                heapq.heappop(pq)
                preD = -1
                cnt -= 1
            print(pq, reverse_pq)
    if cnt:
        if cnt == 1:
            if preD:
                if preD == 1:
                    print(-reverse_pq[0], -reverse_pq[0])
                else:
                    print(pq[0], pq[0])
            else:
                print(-heapq.heappop(reverse_pq), heapq.heappop(pq))
        else:
            print(-heapq.heappop(reverse_pq), heapq.heappop(pq))
    else:
        print('EMPTY')