import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


for _ in range(int(input())):
    pq = []
    reverse_pq = []
    pq_dict = dict()
    cnt = 0
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if a == 'I':
            heapq.heappush(pq, -int(b))
            heapq.heappush(reverse_pq, int(b))
            pq_dict[int(b)] = pq_dict.get(int(b), 0) + 1
            cnt += 1
        elif cnt:
            if a == 'D' and int(b) == 1:
                pq_dict[-heapq.heappop(pq)] -= 1
            elif a == 'D' and int(b) == -1:
                pq_dict[heapq.heappop(reverse_pq)] -= 1
            cnt -= 1
    print(pq_dict)