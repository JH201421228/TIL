import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    K = int(input())
    K_list = list(map(int, input().split()))
    heapq.heapify(K_list)
    ans = 0
    print(K_list)
    while True:
        temp = 0
        a = heapq.heappop(K_list)
        b = heapq.heappop(K_list)
        temp = a + b
        print(a, ' + ', b, ' = ', temp)
        # temp += heapq.heappop(K_list)
        # temp += heapq.heappop(K_list)
        # ans += temp
        if K_list:
            heapq.heappush(K_list, temp)
            print(K_list)
        else:
            print(ans)
            break