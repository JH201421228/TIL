import sys
import heapq
sys.stdin = open('input.txt')
input=sys.stdin.readline
mx = sys.maxsize

def main():
    n = int(input())
    m = int(input())
    bus = [dict() for _ in range(n+1)]
    for _ in range(m):
        x, y, d = map(int, input().split())
        if y in bus[x]:
            bus[x][y] = min(bus[x][y], d)
        else:
            bus[x][y] = d
    start, end = map(int, input().split())
    heap = [(0, start, [start])]
    dist = [mx] * (n+1)
    while heap:
        cur_dist, cur_node, cur_list = heapq.heappop(heap)
        if cur_node == end:
            print(cur_dist)
            print(len(cur_list))
            for i in range(len(cur_list)):
                print(cur_list[i], end=' ')
            sys.exit()
        if dist[cur_node] < cur_dist:
            continue
        for b, c in bus[cur_node].items():
            if dist[b] <= cur_dist + c:
                continue
            dist[b] = cur_dist + c
            heapq.heappush(heap, (cur_dist + c, b, cur_list + [b]))


main()