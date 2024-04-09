import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


for _ in range(int(input())):
    pq = [] # 작은 수 부터 꺼냄
    re_pq = [] # 큰 수 부터 꺼냄
    cnt_in_q = 0 # 현재 큐에 들어있는 숫자 갯수
    q_dict = dict() # 큐에 어떤 숫자가 들어있는지
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if a == 'I':
            heapq.heappush(pq, int(b))
            heapq.heappush(re_pq, -int(b))
            cnt_in_q += 1
            q_dict[int(b)] = q_dict.get(int(b), 0) + 1
        elif a == 'D' and int(b) == 1: # 최대값을 삭제하는 연산
            if cnt_in_q:
                while q_dict[-re_pq[0]] <= 0: # 실제로 큐에 들어있는지 찾는 작업
                    heapq.heappop(re_pq)
                n = -heapq.heappop(re_pq)
                cnt_in_q -= 1
                q_dict[n] -= 1
        elif a == 'D' and int(b) == -1: # 최솟값을 삭제하는 연산
            if cnt_in_q:
                while q_dict[pq[0]] <= 0:
                    heapq.heappop(pq)
                n = heapq.heappop(pq)
                cnt_in_q -= 1
                q_dict[n] -= 1

        if not cnt_in_q:
            pq, re_pq = [], []
            q_dict = dict()

    if cnt_in_q:
        while q_dict[-re_pq[0]] <= 0:
            heapq.heappop(re_pq)
        max_num = -heapq.heappop(re_pq)
        while q_dict[pq[0]] <= 0:
            heapq.heappop(pq)
        min_num = heapq.heappop(pq)
        print(max_num, min_num)
    else:
        print('EMPTY')
